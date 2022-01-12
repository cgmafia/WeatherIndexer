import flask
from flask import request, jsonify
from flask import json
from pathlib import Path
import weather as w

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> Test </h1><p> api endpoint for test /check </p>"

@app.route('/check', methods=['GET'])
def check():
    if 'city' in request.args:
        city = request.args.get('city')
        print(city)
        result = w.main(city)
        return result
    else:
        return { "error": "True" }


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The page could not be found.</p>", 404




app.run()