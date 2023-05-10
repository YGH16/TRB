from flask import Flask, session, request, flash, render_template
from pymongo import MongoClient
import certifi

app = Flask(__name__)
app.secret_key = 'fUjXn2r5u8x!A%D*G-KaPdSgVkYp3s6v'
ca = certifi.where()

client = MongoClient('mongodb+srv://TRP:ZivIortmj3k8olHW@cluster0.uw2qkum.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

try:
    client.admin.command('ping')
    print("Successfully pinged db")
    database = client['TRB']
except Exception as e:
    print(e)

@app.route("/")
def loadIndexPage():
    return "Hello Gangsta"

@app.route("/login", methods=["GET", "POST"])
def displayLoginPage():
    if request.method == "GET":
        return "Login Page"
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        user_db = database['users']
        # Check user exists
        user = user_db.find_one({'username': username})
        if user:
            if user['password'] == password:
                session['username'] = username
                session['logged_in'] = True
                print("testing111")
            
                return "Successfully Logged in"
            return "Incorrect credentials, try again"
        else:
            return "This Account does not exist"
    
@app.route("/register", methods=["GET", "POST"])
def displayRegisterPage():
    if request.method == "GET":
        return "Register Page"
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        user_db = database['users']
        # Check if user already exists
        user_status = user_db.find_one({"username": username})

        if user_status:
            return "this user already exists"

        user = {'username': username, 'password': password, 'email': email}
        x = user_db.insert_one(user)

        return "Successfully Registered"
    

@app.route("/create_recipe", methods=["POST"])
def createRecipe():
    if session["username"] and session['logged_in']:
        recipe_name = request.form.get('name')
        time_taken = request.form.get('time_taken')
        recipe_body = request.form.get('recipe_body')

        recipe_list = database['recipes']
        recipe = {"name":recipe_name, "time_taken": time_taken, "body": recipe_body}

        recipe_list.insert_one(recipe)
    
    return "hello"








