from flask import Flask, json, request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.router('/')
def index():
    return '<h1>Hello men</h1>'