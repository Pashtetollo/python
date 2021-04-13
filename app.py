  
from flask import Flask, request, jsonify, abort, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import re


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

deleted = set()

class Fruit(db.Model):
    __tablename__ = 'fruit'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False, nullable=False)
    color = db.Column(db.String(20), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    season = db.Column(db.String(20), unique=False, nullable=False)


class FruitSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'color', 'price', 'season')


@app.route("/", methods=["GET"])
def get_fruits():
    fruit = Fruit.query.all()
    return jsonify(FruitSchema(many=True).dump(fruit))

@app.route("/name=<name>", methods=["GET"])
def get_fruits_by_name(name):
    fruit = Fruit.query.filter(Fruit.name == name)
    if not fruit:
        abort(404)
    return jsonify(FruitSchema(many=True).dump(fruit))

@app.route("/name=<name>&color=<color>&season=<season>&price&lt=<price>", methods=["GET"])
def get_ultimate_fruit(name, color, season, price):
    fruit = Fruit.query.filter(
        #Чому пошук залежить від порядку при операторі or ? (якщо поміняти місцями то приймає лише "any" а так працюють обидві умови)
        (name == "any") or (Fruit.name == name),             
        (color == "any") or (Fruit.color == color),
        (season == "any") or (Fruit.season == season),
        (price == "any") or (Fruit.price <= price))
    if not fruit:
        abort(404)
    return jsonify(FruitSchema(many=True).dump(fruit))
    
@app.route("/color=<color>", methods=["GET"])
def get_fruits_by_color(color):
    fruit = Fruit.query.filter(Fruit.color == color)
    if not fruit:
        abort(404)
    return jsonify(FruitSchema(many=True).dump(fruit))

@app.route("/season=<season>", methods=["GET"])
def get_fruits_by_season(season):
    fruit = Fruit.query.filter(Fruit.season == season)
    if not fruit:
        abort(404)
    return jsonify(FruitSchema(many=True).dump(fruit))

@app.route("/price&lt=<price>", methods=["GET"])
def get_fruits_by_price(price):
    fruit = Fruit.query.filter(Fruit.price <= price)
    if not fruit:
        abort(404)
    return jsonify(FruitSchema(many=True).dump(fruit))

@app.route("/<id>", methods=["GET"])
def get_fruit(id):
    fruit = Fruit.query.get(id)
    if not fruit:
        if id in deleted:
            abort(410)
        else:
            abort(404)
    return jsonify(FruitSchema().dump(fruit))
    

@app.route("/", methods=["POST"])
def add_fruit():
    fruit = Fruit(
     name = request.json["name"],
     color = request.json["color"],
     price = request.json["price"],
     season = request.json["season"])
    db.session.add(fruit)
    db.session.commit()
    return make_response(jsonify(
     id = str(fruit.id),
     name = request.json["name"],
     color = request.json["color"],
     price = request.json["price"],
     season = request.json["season"],
     status = "success",
     adress = request.base_url + str(fruit.id)), 
     201)


@app.route("/<id>", methods=["DELETE"])
def delete_fruit(id):
    fruit = Fruit.query.get(id)
    if not fruit:
        if id in deleted:
            abort(410)
        else:
            abort(404)
    deleted.add(id)
    db.session.delete(fruit)
    db.session.commit()
    return  make_response(jsonify(status = "success"), 204)

@app.route("/<id>", methods=["PUT"])
def update_fruit(id):
    fruit = Fruit.query.get(id)
    if not fruit:
        abort(404)
    fruit.name = request.json["name"]
    fruit.color = request.json["color"]
    fruit.price = request.json["price"]
    fruit.season = request.json["season"]
    db.session.commit()
    return make_response(jsonify(status = "success"), 200)


if __name__ == '__main__':
    app.run(debug=True)