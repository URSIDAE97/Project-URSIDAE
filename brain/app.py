from flask import Flask, render_template

from api import *


app = Flask(__name__)
app.register_blueprint(test_api)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5656, debug=True)
