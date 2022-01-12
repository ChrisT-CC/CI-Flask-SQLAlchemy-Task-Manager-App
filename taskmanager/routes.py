from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


# Create a basic app route using the root-level directory of "/"
@app.route("/")
def home():
    return render_template("base.html")
