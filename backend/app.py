from flask import Flask
from flask_cors import CORS
from request import return_query
import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/search/<string:value>')
def index(value):
    query = return_query(value)
    req = requests.get(query)
    return (req.json())


if __name__ == '__main__':
    print()
    app.run(host='0.0.0.0', port=5000, debug=True)