from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy as sql
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:pindrajora@localhost:5432/assign"

db = sql(app)


class Buyer(db.Model):
    __tablename__ = "buyer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(10))
    password = db.Column(db.String(100))


class Seller(db.Model):
    __tablename__ = "seller"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(10))
    password = db.Column(db.String(100))


class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    sid = db.Column(db.Integer, db.ForeignKey("seller.id"))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Cart(db.Model):
    __tablename__ = "cart"
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    quantity = db.Column(db.Integer)
    buyer_id = db.Column(db.Integer, db.ForeignKey("buyer.id"))
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.id"))


@app.route("/seller", methods=["GET"])
def get_all_seller():
    users = Seller.query.all()

    out = []

    for seller in users:
        data = {}
        data["id"] = seller.id
        data["public_id"] = seller.public_id
        data["name"] = seller.name
        data["email"] = seller.email
        data["phone"] = seller.phone
        data["address"] = seller.address
        out.append(data)
    return jsonify({"seller": out})


@app.route("/seller/<public_id>", methods=["GET"])
def get_seller(public_id):
    seller = Seller.query.filter_by(public_id=public_id).first()

    if not seller:
        return jsonify({"message": "No user Found"})

    data = {}
    data["id"] = seller.id
    data["public_id"] = seller.public_id
    data["name"] = seller.name
    data["email"] = seller.email
    data["phone"] = seller.phone
    data["address"] = seller.address

    return jsonify({"seller": data})


@app.route("/seller", methods=["POST"])
def create_seller():
    try:
        data = request.get_json()
        password = generate_password_hash(data["password"], method="sha256")

        newUser = Seller(
            public_id=str(uuid.uuid4()),
            email=data["email"],
            name=data["name"],
            password=password,
            address=data["address"],
            phone=data["phone"],
        )
        db.session.add(newUser)
        db.session.commit()
    except:
        return jsonify({"message": "some error occured"})
    return jsonify({"message": "New Seller created successfully"})


@app.route("/buyer", methods=["GET"])
def get_all_buyer():
    users = Buyer.query.all()

    out = []

    for buyer in users:
        data = {}
        data["id"] = buyer.id
        data["public_id"] = buyer.public_id
        data["name"] = buyer.name
        data["email"] = buyer.email
        data["phone"] = buyer.phone
        data["address"] = buyer.address
        out.append(data)
    return jsonify({"seller": out})


@app.route("/buyer/<public_id>", methods=["GET"])
def get_buyer(public_id):
    buyer = Buyer.query.filter_by(public_id=public_id).first()

    if not buyer:
        return jsonify({"message": "no buyer found"})

    data = {}
    data["id"] = buyer.id
    data["public_id"] = buyer.public_id
    data["name"] = buyer.name
    data["email"] = buyer.email
    data["phone"] = buyer.phone
    data["address"] = buyer.address

    return jsonify({"buyer": data})


@app.route("/buyer", methods=["POST"])
def create_buyer():
    try:
        data = request.get_json()
        password = generate_password_hash(data["password"], method="sha256")

        newUser = Buyer(
            public_id=str(uuid.uuid4()),
            email=data["email"],
            name=data["name"],
            password=password,
            address=data["address"],
            phone=data["phone"],
        )
        db.session.add(newUser)
        db.session.commit()
    except:
        return jsonify({"message": "some error occured"})
    return jsonify({"message": "New Seller created successfully"})


@app.route("/item", methods=["POST"])
def create_item():
    try:
        data = request.get_json()
        newItem = Item(
            name=data["name"],
            sid=data["sid"],
            quantity=data["quantity"],
            price=data["price"],
        )
        db.session.add(newItem)
        db.session.commit()
    except:
        return jsonify({"message": "some error occured"})

    return jsonify({"message": "New item created"})


@app.route("/item/<sid>", methods=["GET"])
def get_all_item_of_seller(sid):
    items = Item.query.filter_by(sid=sid).all()
    if not items:
        return jsonify({"message": "no item found"})

    out = []
    for item in items:
        data = {}
        data["id"] = item.id
        data["sid"] = item.sid
        data["quantity"] = item.quantity
        data["price"] = item.price
        data["name"] = item.name
        out.append(data)

    return jsonify({"items": out})


@app.route("/item/<sid>/<item_id>", methods=["GET"])
def get_all_item_of_seller_itemid(sid, item_id):
    items = Item.query.filter_by(sid=sid, id=item_id).all()
    if not items:
        return jsonify({"message": "no item found"})

    out = []
    for item in items:
        data = {}
        data["id"] = item.id
        data["sid"] = item.sid
        data["quantity"] = item.quantity
        data["price"] = item.price
        data["name"] = item.name
        out.append(data)

    return jsonify({"items": out})


@app.route("/cart", methods=["POST"])
def create_cart():
    try:
        data = request.get_json()
        newCart = Cart(
            item_id=data["item_id"],
            quantity=data["quantity"],
            buyer_id=data["buyer_id"],
            seller_id=data["seller_id"],
        )
        db.session.add(newCart)
        db.session.commit()
    except:
        return jsonify({"message": "some error occured"})

    return jsonify({"message": "New item added"})


@app.route("/cart/<sid>/<bid>", methods=["GET"])
def get_cart_sid_bid(sid, bid):
    carts = Cart.query.filter_by(seller_id=sid, buyer_id=bid).all()

    if not carts:
        return jsonify({"message": "not cart found"})

    out = []
    for cart in carts:
        data = {}
        data["item_id"] = cart.item_id
        data["quantity"] = cart.quantity
        data["buyer_id"] = cart.buyer_id
        data["seller_id"] = cart.seller_id
        out.append(data)

    return jsonify({"cart": out})


if __name__ == "__main__":
    app.run(debug=True)
