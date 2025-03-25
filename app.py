import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Привет от приложения Flask1</h1>"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
