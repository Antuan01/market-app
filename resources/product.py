from flask_restful import Resource, reqparse
from models.Product import Product, ProductSchema
from models.User import User, UserSchema
from flask import request

class ProductResource(Resource):

    def get(self, id):
        return ProductSchema().dump(Product.query.get(id))

    def post(self, id):
        product = Product.query.get(id)
        product.name = request.form["name"]
        product.price = request.form["price"]
        product.stock = request.form["stock"]
        product.update()
        return ProductSchema().dump(product), 201

    def delete(self, id):
        trash = Product.query.get(id)
        trash.delete()
        return "", 204 

class ProductList(Resource):

    def get(self):
        return ProductSchema(many=True).dump(Product.query.all())

    def post(self):
        data = Product(name=request.form["name"],
                price=request.form["price"],
               stock=request.form["stock"]
                )
        data.create()
        return ProductSchema().dump(data), 201
