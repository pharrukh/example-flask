import logging
import azure.functions as func
from flask import Flask, request
import os
import sys

app = Flask(__name__)


@app.route('/',  methods=['POST', 'GET'])
def hello_world():
    return 'Hello World!'


@app.route('/hi',  methods=['POST', 'GET'])
def hi():
    return 'Hi World!'


@app.route('/hello')
@app.route('/hello/<name>', methods=['POST', 'GET'])
def hello(name=None):
    return name != None and 'Hello, '+name or 'Hello, '+request.args.get('name')


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('here')
    return func.WsgiMiddleware(app).handle(req, context)
