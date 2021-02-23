from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os


SECRET_KEY = os.urandom(42)

# instantiate flask app
app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'myapp.db')
db_uri = 'sqlite:///{}'.format(db_path)
print(db_uri)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

from app import routes, models
from app.models import User
db.create_all()
