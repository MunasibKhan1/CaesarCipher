from flask import Flask, render_template, request
from encrypt import encrypt
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypted():
    message = request.form.get("msg")
    key =  int(request.form.get("key"))
    count = encrypt(key, message)
    return render_template("index.html", counts=count)

