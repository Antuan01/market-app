from db import db, ma
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()

class OrderSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "price", "quantity")
