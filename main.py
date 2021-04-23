import json
import requests
from flask import Flask, Response, render_template, request

app = Flask(__name__)


def call_github(username):
    try:
        github_api = 'https://api.github.com/users'
        response = requests.get(f'{github_api}/{username}/repos')
    except requests.exceptions.RequestException as error:
        print(error)
        return Response(status=404)
    else:
        return response


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/repos/<username>')
def repos(username):
    """Get info about all repos for a given user,
        then create json with repository name and number of stars

    Args:
        username (string): GitHub username to check

    Returns:
        [Response]: Returns json with data if status code is 200.
    """
    response = call_github(username)
    if response.status_code == 200:
        data_all = {}
        for r in response.json():
            data = {'watchers': r['watchers_count']}
            data_all[r['name']] = data
        return Response(json.dumps(data_all), status=200, mimetype='application/json')
    return Response(status=400)


@app.route('/stars/<username>')
def stars(username):
    """Get info about all repos for a given user, and sum all stars

    Args:
        username (string): GitHub username to check

    Returns:
        [Response]: Returns sum of all stars if status code is 200
    """
    response = call_github(username)
    if response.status_code == 200:
        stars_sum = 0
        for r in response.json():
            stars_sum += r['watchers_count']
        return Response(json.dumps(stars_sum), status=200, mimetype='application/json')
    return Response(status=400)


@ app.route('/repos_front', methods=['GET', 'POST'])
def repos_front():
    if request.method == 'POST':
        username = request.form['username']
        response = repos(username)
        if response.status_code == 200:
            return render_template("repos.html", username=username, repos=response.json)
        return render_template("index.html", error="Something went wrong")
    return render_template("index.html")


@ app.route('/stars_front', methods=['GET', 'POST'])
def stars_front():
    if request.method == 'POST':
        username = request.form['username']
        response = stars(username)
        if response.status_code == 200:
            return render_template("stars.html", username=username, stars=response)
        return render_template("index.html", error="Something went wrong")
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
