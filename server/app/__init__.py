from flask import Flask
from flask_crontab import Crontab
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager #Inisialisasi JWT
from flask_mail import Mail

app = Flask(__name__)
crontab = Crontab(app)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
mail = Mail(app)

from app.model import user, post, word_cloud, api_config, notification, help
from app import routes

