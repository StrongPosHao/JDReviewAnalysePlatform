#encoding: utf-8

from exts import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.Text, nullable=False)
    information = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(20), db.ForeignKey('product.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.SmallInteger, nullable=False)
    time = db.Column(db.String(30), nullable=False)
    usefulVoteCount = db.Column(db.Integer, nullable=False)
    userExpValue = db.Column(db.Integer, nullable=False)
    images = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    replyCount = db.Column(db.Integer, nullable=False)
    afterComment = db.Column(db.Integer, nullable=False)
    product_type = db.Column(db.String(200), nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(20), nullable=False)