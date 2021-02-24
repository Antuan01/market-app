from db import db, ma
from datetime import datetime

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.relationship("Address", backref="person", lazy="select", uselist=False)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return { "name": self.name }

class PersonSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
