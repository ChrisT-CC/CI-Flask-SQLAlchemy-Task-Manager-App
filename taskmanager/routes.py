""" create routes to link the static templates """
from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    """ create a basic app route using the root-level directory of "/" """
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    """ populate the new categories template """
    # add code to query the db to be used in categories template
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


# we need to include a list of the two methods "GET" and "POST", since we will
# be submitting a form to the database
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """ template for adding a new category """
    # POST method functionality for users to add a new category to the database
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        # after the form gets submitted, and we're adding and committing the
        # new data to our database, we could redirect the user back to the
        # 'categories' page
        return redirect(url_for("categories"))
    return render_template("add_category.html")
