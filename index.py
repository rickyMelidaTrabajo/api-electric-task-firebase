from flask import Flask
from routes import route
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './images'

route.route(app)


@app.route('/', methods=['GET', 'POST'])
def main():
    return 'sale'
