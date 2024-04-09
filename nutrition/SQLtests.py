import mysql.connector

# Connection aufbauen
mydb = mysql.connector.connect(
  host="localhost",
  port="52880",
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
print(f"{usersDB}")

# Cursor und Connection schließen
cursor.close()
mydb.close()

"""
    {"name":"Pasta", "cals":373, "carbs":68.6, "fats":3.3, "protein":15.3, "addedby":"Luca"}
    {"name":"Rice", "cals":346, "carbs":67.6, "fats":3.1, "protein":9.8, "addedby":"Luca"}
    {"name":"Nutella", "cals":547, "carbs":56.9, "fats":31.8, "protein":6.6, "addedby":"Luca"}
"""