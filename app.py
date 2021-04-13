  
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

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


@app.route("/<id>", methods=["GET"])
def get_fruit(id):
    fruit = Fruit.query.get(id)
    if not fruit:
        abort(404)
    return jsonify(FruitSchema().dump(fruit))


@app.route("/", methods=["POST"])
def add_fruit():
    fruit = Fruit(name=request.json["name"], color=request.json["color"], price = request.json["price"], season = request.json["season"])
    db.session.add(fruit)
    db.session.commit()
    return jsonify(FruitSchema().dump(fruit))


@app.route("/<id>", methods=["DELETE"])
def delete_fruit(id):
    fruit = Fruit.query.get(id)
    if not fruit:
        abort(404)
    db.session.delete(fruit)
    db.session.commit()
    return jsonify(success=True)


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
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)