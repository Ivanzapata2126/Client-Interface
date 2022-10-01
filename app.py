import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import sys

app = Flask(__name__)
bootstrap = Bootstrap(app)
url_Base = "http://127.0.0.1:5000"


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stores")
def get_stores():
    url_get_stores = url_Base + "/store"
    response = requests.get(url_get_stores)
    data = response.json()
    stores = data['stores']
    return render_template('stores.html',value=stores)

@app.route("/store/<name_store>")
def get_store(name_store):
    url_get_store = url_Base + "/store/" + name_store
    response = requests.get(url_get_store)
    data = response.json()
    return render_template('store.html',value=data)

@app.route("/create_store")
def form_store():
    return render_template('create_store.html')

@app.route("/item_detail",methods=['POST'])
def create_store():
    name = request.form['name']
    url_create_item = url_Base + "/store"
    model = {
        "name": name,
        }
    response = requests.post(url_create_item, json=model)
    data = response.json()
    return render_template('item_detail.html',value=data)

@app.route("/create_item/<name_store>")
def item_form(name_store):
    return render_template('create_item.html',value=name_store)

@app.route("/item_detail/<name_store>",methods=['POST'])
def create_item(name_store):
    name = request.form['name']
    price = request.form['price']
    url_create_item = url_Base + "/store/" + name_store + "/item"
    model = {
        "name": name,
        "price": price,
        }
    response = requests.post(url_create_item, json=model)
    data = response.json()
    return render_template('item_detail.html',value=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)