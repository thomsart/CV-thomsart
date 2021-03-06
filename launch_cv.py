""" !/usr/bin/env python3
    -*- coding: utf-8 -*-

This module is use to execute the server of the site www.thomsart.tech """

import bottle
from bottle import Bottle, route, static_file, template, run

app = Bottle()

@app.route('<filename:path>')
def return_css(filename):
    """ The path to return css files """

    if str(filename) == "/base.css":
        return static_file(filename, root='static/css/')
    else:
        return static_file(filename, root='static/assets/img/')


@app.route('/')
def home():
    """ The path to return the home template """

    return template('home', name=home)


@app.route('/mentions_legales')
def mentions_legales():
    """ The path to return the mentions legales template """

    return template('mentions_legales', name=mentions_legales)


if __name__ == '__main__':
    print('launch on local')
    run(app, host='localhost', port=8080, debug=True, reloader=True)
else:
    print('launch on vps')
    app.run(server='gunicorn')
