from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy
from db import db, ma

from resources.product import ProductResource, ProductList
from resources.orders import OrderResource, OrderList

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
db.app = app
ma.app = app
api = Api(app)

Migrate(app, db)

api.add_resource(ProductResource, '/product/<int:id>')
api.add_resource(ProductList, "/products")

api.add_resource(OrderResource, "/order/<int:id>")
api.add_resource(OrderList, "/orders")


if __name__ == '__main__':
    app.run(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        debug=os.getenv("DEBUG")
        )
