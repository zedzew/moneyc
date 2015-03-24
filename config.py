# -*- coding: utf-8 -*-
import os

class BaseConfig(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(basedir, 'app.db')
    CSRF_ENABLED = True
    SECRET_KEY = 'P\xa1<\t\x13\xbe\xbfI\xeb\x1c#1\x9b\xe2\xfcP'
    WHOOSH_BASE = os.path.join(basedir, 'search.db')

class ProductionConfig(BaseConfig):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
	TESTING = True

'''
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(basedir, 'app.db')
CSRF_ENABLED = True
SECRET_KEY = '\x9a\x0ek\xb6K6\xe5\xc9*\xfa\x8e\\ht\x81\x99\xc6\x80\x85@\x99&\x89\x1f'

'''