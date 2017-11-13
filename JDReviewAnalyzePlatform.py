#encoding: utf-8

from flask import Flask,render_template,request,redirect,url_for,session, g
from exts import db
import config
from models import Reviews,Product,User
import socket

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('user_id'):
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/configuration/')
def configuration():
    configuration = Product.query.all()
    return render_template('configuration.html', configuration = configuration[0].information.split('\n'))

@app.route('/price/')
def price():
    return render_template('price.html')

@app.route('/content/')
def content():
    reviews = Reviews.query.all()
    return render_template('reviews.html', reviews=reviews)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanenet = True
            return redirect(url_for('index'))
        else:
            return u'Telephone or password is incorrect, please check your input and try again!'

@app.route('/signout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'This telephone number has already been used, please change another telephone number and try again!'
        else:
            if password1 != password2:
                return u'The password is different from your first input, please check your input and try again!'
            else:
                user = User(telephone = telephone, username = username, password = password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}

@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user

if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()), port=5000)

