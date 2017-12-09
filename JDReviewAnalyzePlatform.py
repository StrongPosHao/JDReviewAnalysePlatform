#encoding: utf-8

from flask import Flask,render_template,request,redirect,url_for,session, g
from exts import db
import config
from models import Reviews,Product,User
import socket
import os
import codecs
from SplitReview import SplitReview

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # insertDB()
    if session.get('user_id'):
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

# @app.route('/configuration/')
# def configuration():
#     configuration = Product.query.all()
#     return render_template('configuration.html', configuration = configuration[0].information.split('\n'))

@app.route('/price/')
def price():
    return render_template('basicInfo.html')

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

@app.route('/detail/info/<id>')
def configuration(id):
    basicInfo = Product.query.filter(Product.id == id).first()
    return render_template('configuration.html', infomation = basicInfo.information.split('\r\n'))

@app.route('/detail/basic/<id>')
def basicInfo(id):
    basicInfo = Product.query.filter(Product.id == id).first()
    return render_template('basicInfo.html', id = basicInfo.id, name = basicInfo.name, price = basicInfo.price)

@app.route('/detail/<id>')
def product_detail(id):
    return render_template('detail.html', id = id)

@app.route('/review/<id>')
def review(id):
    reviews = Reviews.query.filter(Reviews.product_id == id).all()
    return render_template('review.html', reviews = reviews)

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


#breakpoint
def insertDB():
   folders = os.listdir(r'D:/Programming/PyCharm workspace/JDReviewAnalyzePlatform/static/Data/')
   i = 0
   for id in folders:
       with codecs.open(r'D:/Programming/PyCharm workspace/JDReviewAnalyzePlatform/static/Data/' + id + '/basicInfo.txt',
                        'r', encoding='utf-8') as f:
           info = f.read().split("--------------------------------------------------------------------------------------------------------")
           productName = info[0].strip()
           price = float(info[1].strip())
           productConfig = info[2]
           product = Product(id = id, information = productConfig, name = productName, price = price)
           db.session.add(product)
           db.session.commit()
       with codecs.open(r'D:/Programming/PyCharm workspace/JDReviewAnalyzePlatform/static/Data/' + id + '/reviews.txt', 'r', encoding='utf-8') as f:
           reviews = f.read().split("-------------------------------------------------------------------------------------------------------------------------------------------------------------\r\n")
           for review in reviews:
               data = review.split("\r\n")
               if data[0] == "":
                   break
               try:
                   content = data[0]  # Review content
                   productId = id
                   # print "productId: " + productId + '\n'
                   score = int(data[2].split(':')[1])       # Review score
                   # print "score: " + str(score) + '\n'
                   creationTime = data[3].split(':')[1]  # Review creationTime
                   # print "creationTime: " + creationTime + '\n'
                   userfulCount = int(data[4].split(':')[1])  # Review usefulCount
                   # print "userfulCount: " + str(userfulCount) + '\n'
                   expValue = int(data[5].split(':')[1])  # Review expValue
                   # print 'expValue: ' + str(expValue) + '\n'
                   images = int(data[6].split(':')[1])  # Review images
                   # print "images: " + str(images) + '\n'
                   length = int(data[7].split(':')[1])  # Review length
                   # print "length: " + str(length) + '\n'
                   count = int(data[8].split(':')[1])  # Review reply count
                   # print "count: " + str(count) + '\n'
                   afterComment = int(data[9].split(':')[1])  # IsAfterComment
                   # print "afterComment: " + str(afterComment) + '\n'
                   productType = data[10].split(':')[1]  # Review productType
                   # print "productType: " + productType + '\n'
                   # print '------------------------------------------------------------------------------------------------\n'
               except Exception, e:
                   continue
               comment = Reviews(product_id=productId, content=content, score=score, time=creationTime,
                                 usefulVoteCount=userfulCount,
                                 userExpValue=expValue, images=images, length=length, replyCount=count,
                                 afterComment=afterComment, product_type=productType)
               db.session.add(comment)
               db.session.commit()

if __name__ == '__main__':
    # app.run(host=socket.gethostbyname(socket.gethostname()), port=5000)
    app.run()

