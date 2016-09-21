from flask import Flask
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['Access-Control-Allow-Origin'] = 'http://183.175.12.157/'
app.config['UPLOAD_FOLDER'] = 'static/'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
from app.view import views
from app.view import foodview, views
from app.view import helpview
from app.view import runview
from app.view import xueview
from app.view import giveview
from app.view import paiview
from app.view import personalview
from app.view import userphoto
from app.view import mineview
from app.view import moneyview
from app.view import imview
from app.view import attentionview
from app.view import refuseview

