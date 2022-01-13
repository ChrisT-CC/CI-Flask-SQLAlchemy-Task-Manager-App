# Task Manager App

This task manager is built using Flask, the SLQAlchemy ORM, and Materialize frontend framework.

This is a [Code Institute](https://codeinstitute.net/) code along project designed to learn:
- how to perform full CRUD functionality, which allows to create, read, update, and delete items on database
- how to create HTML-based user interfaces to demonstrate CRUD calls in action
- how to style these interfaces using the Materialize framework

---

## Set up basic Flask app using the Flask-SQLAlchemy package

- install 2 Python packages `pip3 install Flask-SQLAlchemy psycopg2`
- store sensitive data using environment variables hidden in env.py. Make sure env.py is in .gitignore.
- the app needs to be it's own Python package. So create `taskmanager` folder
- create `__init__.py` file within the taskmanager package, to initialize our taskmanager application as a package, allowing us to use our own imports, as well as any standard imports
- create the new `routes.py` file within the taskmanager package. In it create a basic app route using the root-level directory of "/"
- create `base.html` template in `templates` folder (which is where Flask looks for any HTML templates to be rendered) within the taskmanager package 
- create the main Python file `run.py` that will actually run the entire application. This will be at the root level of the workspace, not part of the taskmanager package itself.

---

## Creating the database

- create the new `models.py` file within the taskmanager package. In it, create 2 separate tables, Category and Task
- import the 2 classes for the tables in `routes.py`
- create taskmanager database: 
    - `set-pg`
    - `psql`
    - `CREATE DATABASE taskmanager`
- use Python to generate and migrate the 2 models into `taskmanager` database.

*__Important__ - if you modify the models later, then you'll need to migrate these changes each time the file is updated with new context.*

    - access the Python interpreter by typing `python3`
    - import the 'db' variable found within the taskmanager package: `>>> from taskmanager import db`
    - perform the .create_all() method: `>>> db.create_all()`
    - exit the Python interpreter: `>>> exit()`

---
Collapse 
## Template inheritance

Creating the front-end user interface in [Materialize](https://materializecss.com/) to interact with the database. Template inheritance was used to extend the html templates, to avoid duplicating code.
- add the CDN link and script tags from the [Materialize 'Getting Started' page](https://materializecss.com/getting-started.html) to `base.html`
- create folder structure for static files. (taskmanager > static > css and js folders)
- link static files to `base.html` using the correct syntax:
    - `{{ url_for('static_folder', filename='path/filename' ) }}`
- add components from Materialize
    - a mobile collapse navbar - initialize side navbar in js
    - a footer - create sticky footer in css
- start using template inheritance functionality using [jinja](https://palletsprojects.com/p/jinja/) blocks to inject content
```
{% extends "base_template_file" %}

{% block content %}
    *Insert content here* 
{% endblock %}
```

---

## Adding categories

Before tasks can be added to the database, we need to have some functionality that handles the categories. 

Building the front-end template that then allows to add new categories to the database.
- create `categories.html` and `add_category.html` templates
- extend the 2 templates from `base.html` template
- create a button that will link the form to add a new category in `categories.html`
- in `routes.py` create a functions that will generate `add_category` and `categories` templates
- create the form to add a category to the database
    - import Materialize text imput code and adjust accordingly
    - create an input field for `category name`
    - create an `ADD CATEGORY` submit button
- in `routes.py` create the `POST` method functionality

---

*Disclaimer: this is a code along project from [Code Institute](https://codeinstitute.net/)'s **Database Management Systems** module*