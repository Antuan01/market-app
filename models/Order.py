from db import db, ma
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.String(20), nullable=False)
    dollar_rate = db.Column(db.String(20), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False, default=0)
    type = db.Column(db.SmallInteger, nullable=False, default=0)
    expiration_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #user_id 
    products = db.relationship('ProductOrder', backref='orders', lazy=True)

    def create(self):
        db.session.add(self)
        db.session.commit()

class OrderSchema(ma.Schema):
    class Meta:
        fields = ("id",
                "total_price", "dollar_rate", "status",
                "type", "expiration_date", "created_at", 
                "updated_at",
                )
