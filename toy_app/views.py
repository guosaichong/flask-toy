from flask import Blueprint, request, render_template, redirect, session
from setting import MONGODB
from flask.json import jsonify
toy = Blueprint("toy", __name__)


@toy.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    user_info = request.form.to_dict()
    user_info_dict = MONGODB.user.find_one(user_info)
    user_info_dict["_id"] = str(user_info_dict["_id"])
    return jsonify(user_info_dict)


@toy.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    user_info = request.form.to_dict()
    res = MONGODB.user.insert_one(user_info)
    if res.inserted_id:
        print("注册成功！")
        return redirect("/login")


@toy.route("/home")
def home():

    return render_template("home.html")
