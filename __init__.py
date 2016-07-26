from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)
from app import views
#from app import views2