from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
<<<<<<< HEAD
    return '<h1>Hello men img="1.jpg"</h1>'
=======
    return '<h1>Hello WORLD</h1>'
>>>>>>> 82a0ef5f520b60066417b3d7d0efb73ac3b52ebb
