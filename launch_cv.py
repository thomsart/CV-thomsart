""" !/usr/bin/env python3
    -*- coding: utf-8 -*-

This module launch the cv on ubuntu vps """

print('launch on vps')

from launch_cv_localy import *

run(app, host='92.222.167.113', port=80, debug=None)