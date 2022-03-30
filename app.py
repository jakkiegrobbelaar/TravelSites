rom flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import routes, models

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)