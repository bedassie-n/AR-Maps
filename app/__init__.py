from flask import Flask
from flask_wtf.csrf import CSRFProtect 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# import the views for flask
from app import views
from app import sqlconnector