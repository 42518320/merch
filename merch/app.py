# Implements a registration form, storing registrants in a SQLite database, with support for dereigstration

import os
import re

from cs50 import SQL
from flask import Flask, render_template, redirect, request, url_for, session
from flask_mail import Mail, Message

app = Flask(__name__)

db = SQL("sqlite:///merch.db")

CLOTHES = [
    "I'm looking to buy only one piece of clothing.",
    "I'm looking to buy multiple pieces of clothing.",
    "I'm not sure how many clothes that I'm willing to buy yet.",
]

@app.route("/")
def index():
    return render_template("index.html", clothes=CLOTHES)



@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    name = request.form.get("name")
    email = request.form.get("email")
    number = request.form.get("number")
    clothes = request.form.get("clothes")
    if not name or not email or not number or clothes not in CLOTHES:
        return render_template("failure.html")

    # Remember registrant
    db.execute("INSERT INTO registrants (name, email, number, clothes) VALUES(?, ?, ?, ?)", name, email, number, clothes)

    # Confirm registration
    return render_template("success.html")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)