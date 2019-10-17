from flask import Flask, render_template

from api import *


app = Flask(__name__)
app.register_blueprint(test_api)


@app.route('/', methods=['GET'])
def info_page():
    return render_template('unauthorized.html'), 401


if __name__ == '__main__':
    app.run(port=5656, debug=True)
