from flask import Flask, Response
import requests
import json

app = Flask(__name__)


def call_github(username):
    try:
        github_api = 'https://api.github.com/users'
        response = requests.get(f'{github_api}/{username}/repos')
    except:
        return Response(status=404)
    else:
        return response


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'test'


@app.route('/repos/<username>')
def repos(username):
    data_all = {}
    response = call_github(username)
    if(response.status_code == 200):
        for r in response.json():
            data = {'watchers': r['watchers_count']}
            data_all[r['name']] = data
        return Response(json.dumps(data_all), status=200, mimetype='application/json')
    else:
        return Response(status=400)


@app.route('/stars/<username>')
def stars(username):
    stars = 0
    response = call_github(username)
    if(response.status_code == 200):
        for r in response.json():
            stars += r['watchers_count']
        return Response(json.dumps(stars), status=200, mimetype='application/json')
    else:
        return Response(status=400)


if __name__ == "__main__":
    app.run(debug=True)
