from flask import Flask
from flask_cors import CORS
from request import return_query
import requests

app = Flask(__name__)
CORS(app)


def filter_result(result):
    """Returns new dictionary"""
    new_result = []
    
    for item in result:
        video = {}
        video["id"] = item["id"]["videoId"]
        video["title"] = item["snippet"]["title"]
        new_result.append(video)

    return new_result



@app.route('/api/search/<string:value>')
def index(value):
    query = return_query(value)
    req = requests.get(f'{query}+basketball')
    result = (req.json())
    
    new_result = filter_result(result["items"])
    return new_result


if __name__ == '__main__':
    print()
    app.run(host='0.0.0.0', port=5000, debug=True)