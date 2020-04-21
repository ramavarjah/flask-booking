from app.models import RestaurantSchema, Restaurant, User
from flask import Blueprint, render_template, jsonify, request
from flask_login import current_user
import json
from sqlalchemy.exc import IntegrityError
from app import db


def __init__(self, **kwargs):
    super(Restaurant, self).__init__(**kwargs)

# Create a Restaurant


def CreateRestaurant(request):
    print("Request is : ", request.json)
    if not request.json:
        return jsonify({'message': 'No input data provided '}), 400
        content = request.get_json()
        content["user_id"] = User.get_current_user().id
        schema = RestaurantSchema()
        restaurantData = schema.load(content)
        newAsset = restaurantData.data
        newAsset["user"] = User.get_current_user()
        a = Restaurant(**newAsset)
        db.session.add(a)
    try:
        db.session.commit()
        return jsonify({"sucess": True})
    except IntegrityError as err:
        print("Error", err)
        return jsonify({"sucess": False})
        db.session.rollback()
