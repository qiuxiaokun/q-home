#encoding: utf8
from flask import Blueprint, render_template

work = Blueprint('work', __name__)

@work.route('/note/')
def note():
    return u'正在努力搬迁中……'
