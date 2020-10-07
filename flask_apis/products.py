from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# Init App with flask

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

# Setup Database with sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize the database
db = SQLAlchemy(app)

# initialize mashmallow for object serialization/deserialization
ma = Marshmallow(app)

# Product class which models the product database table

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    desc = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, desc, price, qty):
        self.name = name
        self.desc = desc
        self.price = price
        self.qty = qty

# Class for creating a schema --Abstraction

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'desc', 'price', 'qty')

# Initialize the above schema

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Creating endpoints
# endpoint for inserting a single product in db
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    desc = request.json['desc']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, desc, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# endpoint for getting all products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result)

# endpoint for getting a specific product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    # result = products_schema.dump(product)

    return product_schema.jsonify(product)

# endpoint for deleting a specific product
@app.route('/product/<id>', methods=['DELETE'])
def del_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


