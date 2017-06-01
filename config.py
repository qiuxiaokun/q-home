#coding: utf8 
import os
import datetime

def get_path(rpath):
    LOCAL_DIR = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(LOCAL_DIR, rpath))

class Config(object):
    MONGODB_SETTINGS = {
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'DB': 'blog',
    }
