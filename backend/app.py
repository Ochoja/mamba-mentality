from flask import Flask, jsonify
from flask_cors import CORS
from request import return_query
# import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/search/<string:value>')
def index(value):
    query = return_query(value)
    # req = requests.get(query)
    # return jsonify(req)
    return query


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)