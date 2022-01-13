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


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """ update the Category text in the Database """
    # create the "category" variable, so that the function to know which
    # specific category to load by using '.get_or_404(category_id)', which
    # queries the db and attempts to find the specified record using the data
    # provided, and if no match is found, it will trigger a 404 error page
    category = Category.query.get_or_404(category_id)
    # "POST" method functionality
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    # "GET" method functionality
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    """ delete a Category in the Database """
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    """ template for adding a new task """
    categories = list(Category.query.order_by(Category.category_name).all())
    # POST method functionality for users to add a new category to the database
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        # after the form gets submitted, and we're adding and committing the
        # new data to our database, we could redirect the user back to the
        # 'categories' page
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)
