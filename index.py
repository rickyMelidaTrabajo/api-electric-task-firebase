from flask import Flask
from routes import route

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './images'

route.route(app)


@app.route('/', methods=['GET', 'POST'])
def main():
    return 'sale'
