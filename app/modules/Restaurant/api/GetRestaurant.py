from flask import (
    request,
    jsonify
)

from app.models import User, UserSchema, Restaurant, RestaurantSchema
from flask_login import current_user
from marshmallow import pprint


def __init__(self, **kwargs):
    super(Restaurant, self).__init__(**kwargs)


def GetRestaurant(request):
    print(current_user.get_id())
    restaurantdetails = Restaurant.query.filter_by(
        id=current_user.get_id()).first()
    schema = RestaurantSchema()
    pprint(schema.dump(restaurantdetails).data)
    restaurant_details = schema.dump(restaurantdetails).data

    if request == None:
        return restaurant_details
    return jsonify(restaurant_details)
