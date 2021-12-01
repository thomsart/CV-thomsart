""" !/usr/bin/env python3
    -*- coding: utf-8 -*-

This module launch the cv on ubuntu vps """

print('launch on vps')

from launch_cv_localy import *

# app = bottle.default_app()
run(host='0.0.0.0', port=80)