from flask import Flask, render_template, jsonify, redirect, url_for
import pandas as pd
import json
from json2html import *

app = Flask(__name__)

df = pd.read_csv("addresses.csv")


@app.route("/")
def home():
    with open("csvjson.json") as obj:
        data = obj.read()
    return render_template("index.html", title="page", jsonfile=json.dumps(data))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()
