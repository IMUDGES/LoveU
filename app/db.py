from app import app
from flask import Flask
from flask_script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
import pymysql

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/loveu'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@183.175.14.250:3306/loveu'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class User(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    UserPhone = db.Column(db.String)
    PassWord = db.Column(db.String)
    NickName = db.Column(db.String)
    TrueName = db.Column(db.String)
    UserSex = db.Column(db.Integer)
    UserGrade = db.Column(db.String)
    UserPhoto = db.Column(db.String)
    SecretKey = db.Column(db.String)
    UserMajor = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserPhone


class Checkcode(db.Model):
    CheckId = db.Column(db.Integer, primary_key=True)
    UserPhone = db.Column(db.String)
    CheckCode = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserPhone + "&" + str(self.CheckCode)


class Class(db.Model):
    ClassId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    Day = db.Column(db.Integer)
    Number = db.Column(db.Integer)
    Information = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.UserId


class Config(db.Model):
    ConfigId = db.Column(db.Integer, primary_key=True)
    Version = db.Column(db.Integer)
    Url = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.ConfigId


class Food(db.Model):
    FoodId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    FoodArea = db.Column(db.String(120))
    FoodInformation = db.Column(db.String(120))
    GetUser = db.Column(db.String(120))
    FoodTime = db.Column(db.DateTime)
    FoodWay = db.Column(db.String)
    State = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Give(db.Model):
    GiveId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    GiveInformatinon = db.Column(db.String)
    GiveImage = db.Column(db.String)
    GetUser = db.Column(db.Integer)
    State = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class GiveComment(db.Model):
    CommentId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    CommentInformation = db.Column(db.String)
    GiveId = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Help(db.Model):
    HelpId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    HelpMoney = db.Column(db.Integer)
    DownTime = db.Column(db.DateTime)
    HelpInformation = db.Column(db.String)
    GetUser = db.Column(db.Integer)
    State = db.Column(db.Integer)
    Finish = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Jwxt(db.Model):
    JwxtId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    JwxtNumber = db.Column(db.String)
    JwxtPassword = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Money(db.Model):
    MoneyId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    Money = db.Column(db.Integer)
    PayPassword = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Pai(db.Model):
    PaiId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    PaiMoney = db.Column(db.Integer)
    UpTime = db.Column(db.DateTime)
    DownTime = db.Column(db.DateTime)
    PaiInformation = db.Column(db.String)
    PaiImage = db.Column(db.String)
    PaiTitle = db.Column(db.String)
    GetUser = db.Column(db.Integer)
    State = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserId


class PaiComment(db.Model):
    CommentId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    CommentInformation = db.Column(db.String)
    PaiId = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Run(db.Model):
    RunId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    RunInformation = db.Column(db.String)
    GetUser = db.Column(db.Integer)
    RunTime = db.Column(db.DateTime)
    State = db.Column(db.Integer)
    RunArea = db.Column(db.String, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Xue(db.Model):
    XueId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer)
    XueArea = db.Column(db.String)
    XueInformation = db.Column(db.String)
    GetUser = db.Column(db.Integer)
    XueTime = db.Column(db.DateTime)
    State = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


if __name__ == '__main__':
    manager.run()
