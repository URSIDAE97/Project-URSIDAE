from flask import Flask
from api import *
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
app.register_blueprint(authentication_api, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(port=6969, debug=True)
