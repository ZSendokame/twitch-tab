from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='./source', static_folder='./source/static')

@app.get('/')
def root():
    get = requests.get('https://api.github.com/users/' + request.args.get('username'))
    username = get.json()['name']
    biography = get.json()['bio']
    followerCount = get.json()['followers']

    return render_template('index.html', username=username, biography=biography, followerCount=followerCount)

app.run()