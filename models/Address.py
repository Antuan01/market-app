from db import db, ma
from datetime import datetime

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("persons.id"))

    def create(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return { "name": self.street }

class AddressSchema(ma.Schema):
    class Meta:
        fields = ("id", "street")
