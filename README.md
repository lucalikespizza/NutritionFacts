# NutritionFacts
Webseite und Server geschrieben in Python für das WPM Hacking mit Python. Hochschule Albstadt-Sigmaringen, SS 2024.

## API-Aufrufe
### Add food
```
Invoke-WebRequest -Uri http://127.0.0.1:5000/foods/add -Method POST -ContentType 'application/json' -Body '{"name":"[Name of Food]", "addedby":[User], "calories":0, "carbs":0, "fats":0, "protein":0}'
```

### Add User

```
Invoke-WebRequest -Uri http://127.0.0.1:5000/users/add -Method POST -ContentType 'application/json' -Body '{"name":"[Username]", "email_address:"[E-Mail-Address]","password":"[Secure PW]"}'
```

## SQL-Aufrufe via Python
### Get all Users
```python
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
```

### User anlegen
```python
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

# Befehl definieren
add_user = ("INSERT INTO users "
            "(name, email_address, password) "
            "VALUES (%(name)s, %(email_address)s, %(password)s)")

# Datensatz definieren
data_user = {
  'name': "Luca",
  'email_address': "luca.monaco@online.de",
  'password': str(hash("secure_af"))
}

# Befehl mit Datensatz ausführen
cursor.execute(add_user, data_user)

# Commit
mydb.commit()

# Cursor und Connection schließen
cursor.close()
mydb.close()
```

### Sessions
```
from flask import session
app.secret_key = "d8Zu^8^g@CNmZ4WkeMAd"

# Add key
session[user] = "Luca"

# Check logged in Status
if "user" in session:
  ...
else:
  ...

# Logout page
@app.route("/logout")
def logout():
  session.pop("user", None)]
  return redirect(url_for("login"))
```

## To-Do

- [ ] Index: if logged in -> Home
- [ ] Login/Register: If logged in -> Home
- [ ] Home: if NOT logged in -> Index
- [ ] Addfood: if NOT logged in -> Index
- [ ] Dont show login/register Button on any Page, if logged in

## Roadmap

- [x] User anlegen per form
- [x] Login per form
- [ ] Logged in status in Session speichern
- [ ] Food anlegen per form
