#encoding: utf-8

from flask import Flask,render_template,request,redirect,url_for,session
from exts import db
import config
from models import Reviews,Information,User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    reviews =  Reviews.query.all()
    infos = Information.query.all()
    return render_template('index.html', reviews = reviews, infos = infos)

if __name__ == '__main__':
    app.run()

