from flask import Flask
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'static/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
from app import views
from app.view import foodview
from app.view import helpview
from app.view import runview
from app.view import xueview
from app.view import giveview
from app.view import personalview

