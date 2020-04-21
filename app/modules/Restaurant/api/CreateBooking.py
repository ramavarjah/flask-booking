from app.models import BookingSchema, Restaurant, User, Booking
from flask import Blueprint, render_template, jsonify, request
from flask_login import current_user
import json
from sqlalchemy.exc import IntegrityError
from app import db


def __init__(self, **kwargs):
    super(Booking, self).__init__(**kwargs)

# Create a Booking


def CreateBooking(request):
    print("Request is : ", request.json)
    if not request.json:
        return jsonify({'message': 'No input data provided '}), 400
    content = request.get_json()
    schema = BookingSchema()
    bookingData = schema.load(content)
    newAsset = bookingData.data
    a = Booking(**newAsset)
    db.session.add(a)
    try:
        db.session.commit()
        return jsonify({"sucess": True})
    except IntegrityError:
        return jsonify({"sucess": False})
        db.session.rollback()
