from flask_restful import Resource, reqparse
from models.product import Product
from flask import request

class Product(Resource):

    def get(self, id):
        return { id: id }

    def post(self, id):
        return { "data": request.form }

    def delete(self, id):
        return { "action": "delete {}".format(id) }

class ProductList(Resource):

    def get(self):
        return { "hola": "bebe" }

    def post(self):
        return { "action": "aqui creo" }
