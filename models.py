#encoding: utf-8

from exts import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.String(10), primary_key=True)
    information = db.Column(db.Text, nullable=False)

class Reviews(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(10), db.ForeignKey('product.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    time = db.Column(db.DateTime, nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(20), nullable=False)