from flask_restful import Resource
from models.product import Product

class ProductResource(Resource):
    def get(self):
        return {"hola": "bebe"}
