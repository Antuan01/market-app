from db import db, ma
from datetime import datetime

class OrderDetail(db.Model):
    __tablename__ = "order_details"
    id = db.Column(db.Integer, primary_key=True)
    #order_id = db.relationship('Orders', backref='order_details', lazy=True)
    #product_id = db.relationship('Products', backref='order_details', lazy=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def create(self):
        db.session.add(self)
        db.session.commit()

#class ProductsSchema(ma.Schema):
#    class Meta:
#        fields = ("unit_price", "quantity")
