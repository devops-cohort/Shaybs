from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@"+os.getenv("MYSQL_URL")+"/"+os.getenv("MYSQL_DB")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bootstrap = Bootstrap(app)
xray_recorder.configure(service='my_app_name')
XRayMiddleware(app, xray_recorder)

from application import routes
