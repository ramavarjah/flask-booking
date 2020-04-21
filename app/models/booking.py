from .. import db


class Booking(db.Model):
    __tablename__ = 'Booking'
    id = db.Column(db.Integer, primary_key=True)
    # booking_date_time_start = db.Column(
    #     db.DateTime, default=datetime.datetime.utcnow())
    # booking_date_time_end = db.Column(
    #     db.DateTime, default=datetime.datetime.utcnow())
    booking_date_time_start = db.Column(db.String(64))
    booking_date_time_end = db.Column(db.String(64))
    people = db.Column(db.Integer)
    MenuOrdered = db.Column(db.String(64))
    BillAmount = db.Column(db.Float)
    PaymentStatus = db.Column(db.String(64))
    PaymentMode = db.Column(db.String(64))
    tables = db.relationship('Table', back_populates="bookings")
    table_id = db.Column(db.Integer, db.ForeignKey('Table.id'))
