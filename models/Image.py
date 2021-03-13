from db import db, ma
from datetime import datetime

class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    imageable_id = db.Column(db.Integer, nullable=False)
    imageable_type = db.Column(db.String(64), nullable=False)
    url = db.Column(db.String(850), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class ImageSchema(ma.Schema):
    class Meta:
        fields = ("url", "id")
