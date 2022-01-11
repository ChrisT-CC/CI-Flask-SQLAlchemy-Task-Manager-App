import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# In order to actually use any of our hidden environment variables, we need to
# import the 'env' package. However, since we are not pushing the env.py file
# to GitHub, this file will not be visible once deployed to Heroku, and will
# throw an error. This is why we need to only import 'env' if the OS can find
# an existing file path for the env.py file itself.
if os.path.exists("env.py"):
    import env  # noqa

# Create an instance of Flask class
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Create an instance of the imported SQLAlchemy() class
db = SQLAlchemy(app)

# Import "routes" file from taskmanager package
from taskmanager import routes  # noqa