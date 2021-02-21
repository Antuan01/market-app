from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from db import db
from resources.product import ProductResource

from models.product import Product

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#db = SQLAlchemy(app)
db.init_app(app)
db.app = app
api = Api(app)

#import config
api.add_resource(ProductResource, '/product')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        debug=os.getenv("DEBUG")
        )
