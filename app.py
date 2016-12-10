import os
import json
from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    desc = db.Column(db.Text)
    image = db.Column(db.Text)
    userid = db.Column(db.Text)
    username = db.Column(db.Text)


    #def __init__(self, title, desc):
    #    self.title = title
    #    self.desc = desc

    #def __repr__(self):
    #    return '<Post %r>' % self.title
    def __init__(self, title, desc, image, userid, username):
        self.title = title
        self.desc = desc
        self.image = image
        self.userid = userid
        self.username = username

db.create_all()

@app.route('/get/', methods = ['GET'])
def index():
    result = { 
        'posts': [] 
    }

    print "get post"

    for post in Post.query.all():
        data = {}
        data['title'] = post.title
        data['desc'] = post.desc
        data['image'] = post.image
        data['userid'] = post.userid
        data['username'] = post.username
        result['posts'].append(data)

    return jsonify(result)
    #return jsonify({'posts': Post.query.all()})


@app.route('/post', methods = ['POST'])
def create_post():
    print "new post"
    content = request.get_json()
    #if not request.json or not 'title' in request.json:
    #    abort(400)
    post = Post(title=content['title'], 
                desc=content['desc'], 
                image=content['image'],
                userid=content['userid'],
                username=content['username'])
    db.session.add(post)
    db.session.commit()
    return 'anything'


if __name__ == '__main__':
    app.run()
#########
