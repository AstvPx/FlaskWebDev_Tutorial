from flask import Flask, request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    ua = request.headers.get('User-Agent')
    return '<p>Flask Web Development. </p><p>User-Agent is : %s .</p>' % ua


@app.route('/user/<name>')
def user(name):
    return '<h2>Hello, %s !</h2>' % name


if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
