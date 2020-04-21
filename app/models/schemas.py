from app import FlaskMarshmallow
from app.models import User, Restaurant, Role, Table, Booking
ma = FlaskMarshmallow()


class RestaurantSchema(ma.ModelSchema):
    class Meta:
        model = Restaurant


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class TableSchema(ma.ModelSchema):
    class Meta:
        model = Table


class BookingSchema(ma.ModelSchema):
    class Meta:
        model = Booking
