from flask import jsonify, request, abort
import inspect
from flask_login import current_user


class ModelAPI:

    allowed_methods = {'list': ['GET'], 'detail':['GET'], 'create': ['POST'], 'update': ['PUT'], 'delete': ['DELETE']}
    fields = "__all__"
    add_path = {}
    auth_required = True

    def __init__(self, db, app, model):
        self.model = model
        self.name = model.__name__
        self.db = db
        for fname, methods in self.allowed_methods.items():
            path = '/%s' % self.name.lower()
            function = getattr(self, fname)
            if function:
                args = inspect.getfullargspec(function).args
                annotations = function.__annotations__
                for param in args[1:]:
                    path += ("/<int:%s>" if annotations.get(param) == int else "/<%s>") % param
            custom_path = self.add_path.get(fname)
            if custom_path:
                path+="/"+custom_path
            app.route(path, methods=methods,endpoint=self.name+"_"+fname)(
                self.check_auth(function) if self.auth_required else function)

    def check_auth(self,function):
        def wrapper(*arg, **kwargs):
            if current_user.is_authenticated:
                return function(*arg,**kwargs)
            return jsonify({"status": "Error","code": "403",
                            "message": "Unauthorized Access Forbidden"}), 403
        return wrapper

    def to_dict(self,obj):
        if self.fields=="__all__":
           return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        return {column: getattr(obj, column) for column in self.fields}

    def to_list(self,query_set):
        return [self.to_dict(obj) for obj in query_set]

    def list(self):
        return jsonify({self.name+"s": self.to_list(self.model.query.all())})

    def create(self):
        if not request.json or not 'name' in request.json:
            abort(400)
        obj = self.model(request.json)
        self.db.session.add(obj)
        self.db.session.commit()
        return jsonify({self.name: self.to_dict(obj)}), 201


    def detail(self, id:int):
        return jsonify({self.name:self.to_dict(self.model.query.get(id))})

    def delete(self, id:int):
        self.db.session.delete(self.model.query.get(id))
        self.db.session.commit()
        return jsonify({'message': "Deleted <%s (%d)> Successfully" % (self.name, id)})


    def update(self, id:int):
        model_obj = self.model.query.get(id)
        for key, val in request.json.items():
            setattr(model_obj,key,val)
        self.db.session.commit()
        return jsonify({self.name: self.to_dict(model_obj)})