# source/my_env/bin/activate

from flask_blog.hello import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


# Steps to run:
"""
export FLASK_APP =hello
export FLASK_ENV=development
flask run
"""