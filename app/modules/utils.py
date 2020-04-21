from flask import (
    Blueprint,
    request
)

from app.modules.Restaurant.api import getCreateRestaurant
from app.modules.Restaurant.api import getCreateDetails
from app.modules.Restaurant.api import getUserDetails
from app.modules.Restaurant.api import getRestaurantDetails
from app.modules.Restaurant.api import getCreateBooking
from app.modules.Restaurant.api import getBookingDetails

thingworx = Blueprint('Api', __name__)

# Registering Routes for Module
getCreateRestaurant(thingworx)  # Login Routes
getCreateDetails(thingworx)
getUserDetails(thingworx)
getRestaurantDetails(thingworx)
getCreateBooking(thingworx)
getBookingDetails(thingworx)
