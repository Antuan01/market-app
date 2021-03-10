from flask_restful import Resource, reqparse
from models.Product import Product, ProductSchema
from models.User import User, UserSchema

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
        return ProductSchema(many=True).dump(Product.query.all())

    def post(self):
        data = Product(name=request.form["name"],
                price=request.form["price"],
               stock=request.form["stock"]
                )
        data.create()

        return ProductSchema().dump(data)
