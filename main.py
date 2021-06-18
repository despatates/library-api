from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
@cross_origin()
def hello():
    """
    Say hello to the world!

    Returns:
        string: Goooood morning!
    """
    return 'Hello, World!'
