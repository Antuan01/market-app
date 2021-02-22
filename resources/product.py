from flask_restful import Resource, reqparse
from models.product import Product
from flask import request

class ProductResource(Resource):

    def get(self, id):
        return { id: id }

    def post(self, id):
        return { "data": request.form }

    def delete(self, id):
        return { "action": "delete {}".format(id) }

class ProductList(Resource):

    def get(self):
        List = [ product.json() for product in Product.query.all()]
        return { "products": List }

    def post(self):

        #Product(request.form).create()
        data = Product(name=request.form["name"],
                price=request.form["price"],
                quantity=request.form["quantity"]
                )
        data.create()
        return { "action": "aqui creo",
                "name": request.form["name"],
                "price": request.form["price"],
                "quantity": request.form["quantity"]               
                }
