from flask import Flask, session
from routes import route
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['UPLOAD_FOLDER'] = './images'

route.route(app)


@app.route('/', methods=['GET', 'POST'])
def main():
    return 'sale'
