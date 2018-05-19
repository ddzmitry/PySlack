from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
from mainscrape import GetData
app = Flask(__name__)
mongo = PyMongo(app)
from bson.json_util import dumps



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    return dumps(mongo.db.slacking_counters.find())

@app.route('/get_initial_scores')
def scrape():
    data = GetData()
    # maybe you can clean tables every time when we scrape
    for i in data:
        print(i)
        mongo.db.slacking_counters.save(i)
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
