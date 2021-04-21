from flask import Flask
import requests
import json

app= Flask(__name__)

def call_github(username):
    data_all = {}
    github_api = 'https://api.github.com/users'
    response = requests.get(f'{github_api}/{username}/repos').json()
    for r in response:
        data = {'watchers': r['watchers_count']}
        data_all[r['name']] = data
    return json.dumps(data_all)

@app.route('/')
def index():
    return call_github('allegro')

if __name__ == "__main__":
    app.run(debug=True)