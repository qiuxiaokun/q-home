#coding: utf8 
from flask import Flask, session, g, url_for, request, redirect
from flask.ext.mongoengine import MongoEngine
import traceback

app = Flask(__name__)
app.config.from_object("config.Config")

# db = MongoEngine()
#db.init_app(app)

from app import views


@app.errorhandler(500)
def errorhandler500(error):
    return error.message

