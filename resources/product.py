import os
from flask_restful import Resource, reqparse
from models.Product import Product, ProductSchema
from models.User import User, UserSchema
from flask import request, url_for, send_from_directory
from models.Image import Image, ImageSchema
from werkzeug.utils import secure_filename

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

    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    def get(self):
        return ProductSchema(many=True).dump(Product.query.all())

    def post(self):
        data = Product(name=request.form["name"],
                price=request.form["price"],
               stock=request.form["stock"]
                )

        data.create()
        #return ProductSchema().dump(data), 201
        if 'file' not in request.files:
            return { "message": "no image" }, 400

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fileurl = url_for('uploaded_file', filename=filename)
            file.save(os.path.join('uploads', filename))
            #return send_from_directory("uploads", filename)
        
        img = Image(url=fileurl,
                imageable_id=data.id,
                imageable_type="product"
                )

        img.create()

        return { "message": fileurl }
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))        

