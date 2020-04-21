from flask import (
    request,
    jsonify
)

from app.models import User, UserSchema
from flask_login import current_user
from marshmallow import pprint
from sqlalchemy.exc import IntegrityError


def GetUser(request):
    print(current_user.get_id())
    userdetails = User.query.filter_by(id=current_user.get_id()).first()
    schema = UserSchema()
    pprint(schema.dump(userdetails).data)
    user_details = schema.dump(userdetails).data
    if request == None:
        return user_details
    return jsonify(user_details)
