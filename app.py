from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'FARREN SUCKS!'

if __name__ == '__main__':
    app.run()