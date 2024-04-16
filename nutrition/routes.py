from nutrition import app
from flask import render_template, request
import mysql.connector

def DB_select_all_users():
    # Connection aufbauen
    mydb = mysql.connector.connect(
    host="localhost",
    port="62885",
    user="nutritionist",
    password="lowcarb",
    database="nutrition_facts_db"
    )
    # Cursor erstellen
    cursor = mydb.cursor()
    # Get all Users
    cursor.execute("select * from users;")
    # Put all Users in usersDB
    usersDB = []
    for (id, name, email_address, password) in cursor:
        usersDB.append({"id":id, "name":name, "email_address":email_address, "password":password})
    cursor.close()
    mydb.close()
    return usersDB

def DB_select_all_foods():
    # Connection aufbauen
    mydb = mysql.connector.connect(
    host="localhost",
    port="62885",
    user="nutritionist",
    password="lowcarb",
    database="nutrition_facts_db"
    )
    # Cursor erstellen
    cursor = mydb.cursor()
    # Get all Foods
    cursor.execute("select * from foods;")
    # Put all Foods in foodsDB
    foodsDB = []
    for (id, name, addedby, cals, carbs, fats, protein) in cursor:
        foodsDB.append({"id":id, "name":name, "addedby":addedby, "cals":cals, "carbs":carbs, "fats":fats, "protein":protein})
    cursor.close()
    mydb.close()
    return foodsDB

def DB_add_new_user(new):
    # Connection aufbauen
    mydb = mysql.connector.connect(
    host="localhost",
    port="62885",
    user="nutritionist",
    password="lowcarb",
    database="nutrition_facts_db"
    )
    # Cursor erstellen
    cursor = mydb.cursor()
    # Post new User
    cursor.execute(f"INSERT INTO users (name, email_address, password) VALUES ('{new['name']}', '{new['email_address']}', '{new['password']}');")
    # Commit
    mydb.commit()
    #Close Cursor and Connection
    cursor.close()
    mydb.close()

def DB_add_new_food(new):
    # Connection aufbauen
    mydb = mysql.connector.connect(
    host="localhost",
    port="62885",
    user="nutritionist",
    password="lowcarb",
    database="nutrition_facts_db"
    )
    # Cursor erstellen
    cursor = mydb.cursor()
    # Post new User
    cursor.execute(f"INSERT INTO foods (name, addedby, cals, carbs, fats, protein) VALUES ('{new['name']}', '{new['addedby']}', '{new['cals']}', '{new['carbs']}', '{new['fats']}', '{new['protein']}');")
    # Commit
    mydb.commit()
    #Close Cursor and Connection
    cursor.close()
    mydb.close()

#Datenbanken updaten
usersDB = DB_select_all_users()
foodsDB = DB_select_all_foods()

# Webpages
@app.route("/")
def page_index():
    return render_template(template_name_or_list="index.html")

@app.route("/home")
def page_home():
    username = "Luca"
    items = DB_select_all_foods()
    print(f"[DEBUG] foodsDB = {foodsDB}")
    return render_template(template_name_or_list="home.html", items=items, username=username)

@app.route('/login')
def login_pages():
    return render_template(template_name_or_list="login.html")

@app.route("/register")
def page_register():
    return render_template(template_name_or_list="register.html")

@app.route("/addfood")
def page_addfood():
    return render_template(template_name_or_list="addfood.html")

# Endpoints
@app.route("/users/login", methods=["POST"])
def login_users():
    new = request.get_json()
    for x in DB_select_all_users():
        print(x)
        if new["name"] == x["name"] and new["password"] == x["password"]:
            print("Nutzername und Passwort korrekt, login genehmigt!")
            return 'OK', 201
    return 'Unauthorized', 401

@app.route("/users/add", methods=["POST"])
def add_user():
    new = request.get_json()
    print(f"[DEBUG] /users/add: Added {new}")
    DB_add_new_user(new)
    return 'OK', 204

@app.route("/foods/add", methods=["POST"])
def add_food():
    new = request.get_json()
    foodsDB.append(new)
    print(f"[DEBUG] /foods/add new = {new}")
    DB_add_new_food(dict(request.get_json()))
    return '', 204

@app.route("/foods/get", methods=["GET"])
def get_foods():
    return DB_select_all_foods()
