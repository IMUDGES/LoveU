from flask import Flask
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)
from app import views
from app.view import foodview
from app.view import helpview
from app.view import runview
from app.view import xueview