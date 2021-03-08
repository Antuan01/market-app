from db import db, ma
from datetime import datetime

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.SmallInteger, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    orders = db.relationship('ProductOrder', backref='products', lazy=True)

    def create(self):
        db.session.add(self)
        db.session.commit()

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "price", "stock", "status", "created_at", "updated_at")
