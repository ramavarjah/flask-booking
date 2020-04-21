from flask import (
    request,
    jsonify
)

from app.models import Booking, BookingSchema
from marshmallow import pprint
from sqlalchemy.exc import IntegrityError


def GetBooking(request):
    print(current_user.get_id())
    bookingdetails = Booking.query.filter_by(id=current_user.get_id()).first()
    schema = BookingSchema()
    pprint(schema.dump(bookingdetails).data)
    booking_details = schema.dump(bookingdetails).data
    if request == None:
        return booking_details
    return jsonify(booking_details)
