""" 
This module is use to execute the server of the site www.thomsart.tech """

import bottle
from bottle import route, static_file, template, run


@route('<filename:path>')
def return_css(filename):
    """ The path to return css files """

    if str(filename) == "/base.css":
        return static_file(filename, root='static/css/')
    else:
        return static_file(filename, root='static/assets/img/')


@route('/')
def home():
    """ The path to return the home template """

    return template('home', name=home)


@route('/mentions_legales')
def mentions_legales():
    """ The path to return the mentions legales template """

    return template('mentions_legales', name=mentions_legales)


if __name__ == '__main__':
    # run(host='localhost', port=8080, debug=True, reloader=True)
    run(host='92.222.167.113', port=80, debug=False)

app = bottle.default_app()