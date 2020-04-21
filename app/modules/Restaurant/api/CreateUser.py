from app.models import RestaurantSchema, Restaurant, User, UserSchema
from flask import Blueprint, render_template, jsonify, request
from flask_login import current_user
import json
from app import db
from sqlalchemy.exc import IntegrityError


def __init__(self, **kwargs):
    super(User, self).__init__(**kwargs)


# Create a User
def CreateUser(request):
    print("Request is : ", request.json)
    if not request.json:
        return jsonify({'message': 'No input data provided '}), 400
    content = request.get_json()
    schema = UserSchema()
    userData = schema.load(content)
    newAsset = userData.data
    a = User(**newAsset)
    db.session.add(a)
    try:
        db.session.commit()
        return jsonify({"sucess": True})
    except IntegrityError:
        return jsonify({"sucess": False})
        db.session.rollback()
