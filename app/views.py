from app import app 
from app import models
from app import forms

@app.route('/')
def hello():
    return "Hello World!"