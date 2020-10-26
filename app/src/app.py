import os
import base64
import requests
import hashlib
from flask import Flask, render_template, request, Response
from flask_redis import FlaskRedis
from io import BytesIO


class Config:
    SECRET_KEY = os.environ.get('APP_SECRET_KEY')
    REDIS_URL = "redis://redis:6379/0"


app = Flask(__name__)
app.config.from_object(Config)
redis = FlaskRedis(app, decode_responses=True)


@app.route('/', methods=['GET'])
def home():
    name = redis.get('name')

    if not name:
        name = 'world'
        redis.set('name', name)

    return render_template('template.html', name=name, avatar_size=256)


@app.route('/set-name', methods=['POST'])
def set_name():
    name = request.form['name']

    redis.set('name', name)

    return Response(name, status=202)


@app.route('/get-monster-avatar/<name>/<size>')
def get_monster_avatar(name, size):
    avatar_base64 = redis.get(name)

    if not avatar_base64:
        salted_name = app.config['SECRET_KEY'] + name
        name_hash = hashlib.sha256(salted_name.encode()).hexdigest()
        response = requests.get('http://monster:8080/monster/' + name_hash + '?size=' + size)
        avatar = response.content
        redis.set(name, base64.b64encode(avatar))
    else:
        avatar = BytesIO(base64.b64decode(avatar_base64))

    return Response(avatar, mimetype='image/png')


if __name__ == "__main__":
    app.run()
