import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import sys

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
url_Base = "http://127.0.0.1:5000"


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stores")
def getStores():
    url_get_stores = url_Base + "/store"
    response = requests.get(url_get_stores)
    data = response.json()
    stores = data['stores']
    return render_template('stores.html',value=stores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)