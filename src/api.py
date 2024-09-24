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

@app.route("/test/")
def test():
    return jsonify({"foo": "bar"})
