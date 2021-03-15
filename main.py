from flask import Flask, send_from_directory
from flask_restful import Resource, Api
from dotenv import load_dotenv
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy
from db import db, ma
from config import Config

from routes import set_routes

load_dotenv()

app = Flask(__name__)

app.config.from_object(Config())
#app.config.from_envvar()

db.init_app(app)
db.app = app
ma.app = app
api = Api(app)

Migrate(app, db)

set_routes(api)

@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        debug=os.getenv("DEBUG")
        )
