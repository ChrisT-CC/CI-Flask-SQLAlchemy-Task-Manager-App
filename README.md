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

---

*Disclaimer: this is a code along project from [Code Institute](https://codeinstitute.net/)'s **Database Management Systems** module*