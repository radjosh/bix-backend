import json
from flask import Flask, jsonify, Response, abort
from flask_cors import CORS

try:
    from .environment_vars import API_KEYS
except ImportError:
    from environment_vars import API_KEYS

'''
for dev server, run with:
    flask --app random_calls run --debug --host=0.0.0.0 --port=5000

for gunicorn, run with:
    gunicorn -w 4 -b 192.241.148.156:5000 'random_calls:app'
'''
# flask boilerplate and kruft
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = API_KEYS['SECRET_KEY']

app.config['DEBUG'] = True
if app.config['DEBUG']:
    app.config["CACHE_TYPE"] = "null"

@app.route("/bix-thing/")
def api():
    DATA = [
        {"name": "Sleve McDichael",
         "attributes": {
            "salary": 100000,
            "title": "Grunt"
        }},
        {"name": "Enrick Bonzalez",
         "attributes": {
            "salary": 1000,
            "title": "Grunt"
        }},
        {"name": "Bob Bobsman",
         "attributes": {
            "salary": 291,
            "title": "CEO"
        }},
        {"name": "Rob Robsbob",
         "attributes": {
            "salary": 29000,
            "title": "Sales"
        }},
        {"name": "Alice Donut",
         "attributes": {
            "salary": 2000,
            "title": "Sales"
        }},
        {"name": "Traynre Observotron",
         "attributes": {
            "salary": 1000,
            "title": "Grunt"
        }}]
    return jsonify(DATA)