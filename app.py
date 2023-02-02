import time

import psycopg2

from flask import Flask

app = Flask(__name__)


@app.get("/")
def hello():
    return 'Hello World! I have been seen you .\n'
