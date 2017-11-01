#encoding: utf-8

from exts import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class Information(db.Model):
    __tablename__ = 'information'
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(200), nullable=False)
    os = db.Column(db.String(50), nullable=False)
    CPU = db.Column(db.String(200), nullable=False)
    memory = db.Column(db.String(200), nullable=False)
    hard_disk = db.Column(db.String(100), nullable=False)
    graphics_card = db.Column(db.String(200), nullable=False)
    drive = db.Column(db.String(100),nullable=False)
    screen = db.Column(db.String(200), nullable=False)
    net = db.Column(db.String(100), nullable=False)
    interface = db.Column(db.String(100), nullable=False)
    Audio = db.Column(db.String(100), nullable=False)
    input = db.Column(db.String(100), nullable=False)
    other_dev = db.Column(db.String(100), nullable=False)
    battery = db.Column(db.String(100),nullable=False)
    size = db.Column(db.String(100), nullable=False)
    feature = db.Column(db.String(50), nullable=True)


class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(20), nullable=False)