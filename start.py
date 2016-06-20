#!/usr/bin/env Python
# coding: utf-8

from flask import Flask

from app.views.index import home

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(home, url_prefix='/home')

if __name__ == '__main__':
    app.run()
