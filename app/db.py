from app import app
from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@183.175.14.250:3306/loveu'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class User(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    UserPhone = db.Column(db.Integer, unique=True)
    PassWord = db.Column(db.String(120), unique=True)
    NickName = db.Column(db.String(120), unique=True)
    TrueName = db.Column(db.String(120), unique=True)
    UserSex = db.Column(db.Integer, unique=True)
    UserGrade = db.Column(db.String(120), unique=True)
    UserPhoto = db.Column(db.String(120), unique=True)
    SecretKey = db.Column(db.String(120), unique=True)
    UserMajor = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserPhone


class Checkcode(db.Model):
    CheckId = db.Column(db.String(120), primary_key=True)
    UserPhone = db.Column(db.String(120), unique=True)
    CheckCode = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserPhone

if __name__ == '__main__':
    manager.run()
