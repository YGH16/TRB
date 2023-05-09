from flask import Flask, session, request

app = Flask(__name__)
app.secret_key = 'fUjXn2r5u8x!A%D*G-KaPdSgVkYp3s6v'

@app.route("/")
def loadIndexPage():
    return "Hello Gangsta"

@app.route("/login", methods=["GET", "POST"])
def displayLoginPage():
    if request.method == "GET":
        return "Login Page"
    else:
        pass

@app.route("/register", methods=["GET", "POST"])
def displayRegisterPage():
    if request.method == "GET":
        return "Register Page"
    else:
        pass





