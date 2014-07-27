import os, flask, utils
from container import app, db


@app.route('/')
def index():
    return 'OK'

