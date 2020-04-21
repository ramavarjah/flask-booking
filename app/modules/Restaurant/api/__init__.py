from .CreateRestaurant import CreateRestaurant
from .CreateUser import CreateUser
from .GetUser import GetUser
from .GetRestaurant import GetRestaurant
from .CreateBooking import CreateBooking
from .GetBooking import GetBooking
from flask import request


def getCreateRestaurant(thingworx):
    @thingworx.route('/restaurant', methods=['POST'])
    def createRestaurant():
        return CreateRestaurant(request)


def getCreateDetails(thingworx):
    @thingworx.route('/createuser', methods=['POST'])
    def createUser():
        return CreateUser(request)


def getUserDetails(thingworx):
    @thingworx.route('/getuser', methods=['GET'])
    def getUser():
        return GetUser(request)


def getRestaurantDetails(thingworx):
    @thingworx.route('/getrestaurant', methods=['GET'])
    def getRestaurant():
        return GetRestaurant(request)


def getCreateBooking(thingworx):
    @thingworx.route('/createbooking', methods=['POST'])
    def createBooking():
        return CreateBooking(request)


def getBookingDetails(thingworx):
    @thingworx.route('/getbooking', methods=['GET'])
    def getBooking():
        return GetBooking(request)
