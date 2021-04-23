from flask import Flask, Response
import requests
import json

app = Flask(__name__)


def call_github(username):
    github_api = 'https://api.github.com/users'
    response = requests.get(f'{github_api}/{username}/repos').json()
    return response


def get_repos_info(username):
    data_all = {}
    response = call_github(username)
    for r in response:
        data = {'watchers': r['watchers_count']}
        data_all[r['name']] = data
    return json.dumps(data_all)


def count_user_stars(username):
    stars = 0
    response = call_github(username)
    for r in response:
        stars += r['watchers_count']
    return json.dumps(stars)


@app.route('/')
def index():
    return 'test'


@app.route('/repos/<user>')
def repos(user):
    return Response(get_repos_info(user), status=200, mimetype='application/json')


@app.route('/stars/<user>')
def stars(user):
    return Response(count_user_stars(user), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)
