#encoding: utf8
from flask import render_template
from app import app
from app.views import work


@app.route('/')
def home():
    # return u'this is homepage'
    return render_template('home.html')

'''
@app.route('/work/note')
def note():
    return '正在努力搬迁中...'
'''

# 注册blueprint
app.register_blueprint(work.work, url_prefix='/work')
# app.register_blueprint(index.index, url_prefix='/')
