from nutrition import app
from flask import render_template, request

itemsDB = [
    {"id":1, "name":"Pasta", "calories":373, "carbs":68.6, "fats":3.3, "protein":15.3, "addedby":"Luca"},
    {"id":2, "name":"Rice", "calories":346, "carbs":67.6, "fats":3.1, "protein":9.8, "addedby":"Luca"},
    {"id":3, "name":"Nutella", "calories":547, "carbs":56.9, "fats":31.8, "protein":6.6, "addedby":"Luca"}
]

usersDB = [
    {"name":"Luca", "pw":hash("hallo")}
]

@app.route("/")
def page_home():
    username = "Luca"
    items = itemsDB
    return render_template(template_name_or_list="home.html", items=items, username=username)

@app.route("/login")
def page_login():
    return render_template(template_name_or_list="login.html")

@app.route("/register")
def page_register():
    return render_template(template_name_or_list="register.html")

@app.route("/users/get", methods=["GET"])
def get_users():
    return usersDB

@app.route("/users/add", methods=["POST"])
def post_user():
    new = dict(request.get_json())
    new["pw"] = hash(new["pw"])
    usersDB.append(new)
    return 'OK', 204

@app.route("/addfood")
def page_addfood():
    return render_template(template_name_or_list="addfood.html")

@app.route("/addfood", methods=["POST"])
def post_addfood():
    itemsDB.append(request.get_json())
    return '', 204