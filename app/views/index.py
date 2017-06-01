#encoding: utf8
from flask import Blueprint, render_template


index = Blueprint('index', __name__)

@index.route('/')
def home():
    # return u'this is homepage'
    return render_template('home.html')
