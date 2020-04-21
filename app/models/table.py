from .. import db


class Table(db.Model):
    __tablename__ = 'Table'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer)
    bookings = db.relationship('Booking', back_populates="tables")
    restaurant = db.relationship('Restaurant', back_populates="tables")
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'))
