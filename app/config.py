from flask import Flask


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'C:/static/'