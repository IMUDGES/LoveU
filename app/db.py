from app import app
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import pymysql

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@183.175.14.250:3306/loveu'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)


class User(db.Model):
    UserId = db.Column(db.Integer, primary_key=True)
    UserPhone = db.Column(db.String, unique=True)
    PassWord = db.Column(db.String, unique=True)
    NickName = db.Column(db.String, unique=True)
    TrueName = db.Column(db.String, unique=True)
    UserSex = db.Column(db.Integer, unique=True)
    UserGrade = db.Column(db.String, unique=True)
    UserPhoto = db.Column(db.String, unique=True)
    SecretKey = db.Column(db.String, unique=True)
    UserMajor = db.Column(db.String, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserPhone


class Checkcode(db.Model):
    CheckId = db.Column(db.Integer, primary_key=True)
    UserPhone = db.Column(db.String, unique=True)
    CheckCode = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserPhone


class Class(db.Model):
    ClassId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    Day = db.Column(db.Integer, unique=True)
    Number = db.Column(db.Integer, unique=True)
    Information = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Config(db.Model):
    ConfigId = db.Column(db.Integer, primary_key=True)
    Version = db.Column(db.Integer, unique=True)
    Url = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.ConfigId


class Food(db.Model):
    FoodId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    FoodArea = db.Column(db.String(120), unique=True)
    FoodInformation = db.Column(db.String(120), unique=True)
    GetUser = db.Column(db.String(120), unique=True)
    FoodTime = db.Column(db.DateTime)
    FoodWay = db.Column(db.String)
    State = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Give(db.Model):
    GiveId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    GiveInformatinon = db.Column(db.String, unique=True)
    GiveImage = db.Column(db.String, unique=True)
    GetUser = db.Column(db.Integer, unique=True)
    State = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class GiveComment(db.Model):
    CommentId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    CommentInformation = db.Column(db.String, unique=True)
    GiveId = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Help(db.Model):
    HelpId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    HelpMoney = db.Column(db.Integer, unique=True)
    DownTime = db.Column(db.DateTime)
    HelpInformation = db.Column(db.String, unique=True)
    GetUser = db.Column(db.Integer, unique=True)
    State = db.Column(db.Integer)
    Finish = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Jwxt(db.Model):
    JwxtId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    JwxtNumber = db.Column(db.String, unique=True)
    JwxtPassword = db.Column(db.String, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Money(db.Model):
    MoneyId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    Money = db.Column(db.Integer, unique=True)
    PayPassword = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Pai(db.Model):
    PaiId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    PaiMoney = db.Column(db.Integer, unique=True)
    UpTime = db.Column(db.DateTime)
    DownTime = db.Column(db.DateTime)
    PaiInformation = db.Column(db.String, unique=True)
    PaiImage = db.Column(db.String, unique=True)
    PaiTitle = db.Column(db.String, unique=True)
    GetUser = db.Column(db.Integer, unique=True)
    State = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.UserId


class PaiComment(db.Model):
    CommentId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    CommentInformation = db.Column(db.String, unique=True)
    PaiId = db.Column(db.String, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Run(db.Model):
    RunId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    RunInformation = db.Column(db.String, unique=True)
    GetUser = db.Column(db.Integer, unique=True)
    RunTime = db.Column(db.DateTime)
    State = db.Column(db.Integer)
    RunArea = db.Column(db.String, unique=True)

    def __repr__(self):
        return '<User %r>' % self.UserId


class Xue(db.Model):
    XueId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, unique=True)
    XueArea = db.Column(db.String, unique=True)
    XueInformation = db.Column(db.String, unique=True)
    GetUser = db.Column(db.Integer, unique=True)
    XueTime = db.Column(db.DateTime)
    State = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.UserId


if __name__ == '__main__':
    manager.run()
