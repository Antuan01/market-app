from db import db, ma
from datetime import datetime

class ProductOrder(db.Model):
    __tablename__ = "product_orders"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.relationship('Orders', backref='product_orders', lazy=True)
    product_id = db.relationship('Products', backref='product_orders', lazy=True)
    price = db.Column(db.String(20), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def create(self):
        db.session.add(self)
        db.session.commit()

class ProductsSchema(ma.Schema):
    class Meta:
        fields = ("price", "quantity")
