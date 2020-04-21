from .. import db


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(64))
    opening_time = db.Column(db.Integer)
    closing_time = db.Column(db.Integer)
    user = db.relationship('User', back_populates="restaurants")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tables = db.relationship('Table', back_populates="restaurant")
