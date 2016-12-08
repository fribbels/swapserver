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


    #def __init__(self, title, desc):
    #    self.title = title
    #    self.desc = desc

    #def __repr__(self):
    #    return '<Post %r>' % self.title
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

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
        result['posts'].append(data)

    return jsonify(result)
    #return jsonify({'posts': Post.query.all()})


@app.route('/post', methods = ['POST'])
def create_post():
    print "new post"
    return


if __name__ == '__main__':
    app.run()
#########


#@app.route("/")

#def hello():
#    return "Hello from Python!"

#if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 5000))
#    app.run(host='0.0.0.0', port=port)