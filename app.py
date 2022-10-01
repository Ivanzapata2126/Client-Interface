import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stores")
def getStores():
    url_get_stores = "http://127.0.0.1:5000/store"
    response = requests.get(url_get_stores)
    data = [(i['name'], i['item']) for i in response.json()]
    return render_template('stores.html',value=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)