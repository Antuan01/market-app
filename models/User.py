from db import db, ma
from datetime import datetime

class User(db.Model):
    __tablemane__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    orders = db.relationship("Order", backref="users", lazy=True) 

    def create(self):
        db.session.add(self)
        db.session.commit()

class UserSchema(User.Schema):
    class Meta:
        fields = ("id", "email")
