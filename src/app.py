import os
import sys

from flask import *
from flask_sqlalchemy import *

# Instantiate the application.
app = Flask(__name__)

# Our database will just be an SQLite database with the name "database.sqlite."
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

# Don't worry about this for now.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Load the database.
db = SQLAlchemy(app)

# Load our models and create all of them in the DB.
from model import *
with app.app_context():
	db.create_all()

# Import our routes from the routes.py file.
from route import *

# Import our API endpoints from the api.py file.
from api import *
