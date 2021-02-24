from db import db, ma
from datetime import datetime

class OrderDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #order_id = db.relationship('Orders', backref='order_details', lazy=True)
    #product_id = db.relationship('Products', backref='order_details', lazy=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    unit_price = db.Column(db.Integer, nullable=False, default=0)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def create(self):
        db.session.add(self)
        db.session.commit()

#class ProductsSchema(ma.Schema):
#    class Meta:
#        fields = ("unit_price", "quantity")
