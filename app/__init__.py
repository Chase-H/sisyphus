from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


# instantiate flask app
app = Flask(__name__)

from app import routes
