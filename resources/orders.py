from flask_restful import Resource, reqparse
from models.Order import Order, OrderSchema
from models.ProductOrder import ProductOrder
from flask import request

class OrderResource(Resource):

    def get(self, id):
        return { id: id }

    def post(self, id):
        return { "data": request.form }

    def delete(self, id):
        return { "action": "delete {}".format(id) }

class OrderList(Resource):

    def get(self):
        return OrderSchema(many=True).dump(Order.query.all())

    def post(self):
        data = Order(total_price=request.form["total_price"],
                dollar_rate=request.form["dollar_rate"],
                status=request.form["status"],
                type=request.form["type"]
                )
        data.create()

        return OrderSchema().dump(data)

