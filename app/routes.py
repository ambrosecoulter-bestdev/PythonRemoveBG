#External Imports
from keyword import kwlist
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from jinja2 import Undefined
from werkzeug.urls import url_parse
import uuid
from datetime import datetime
from turbo_flask import Turbo
from requests import get, post
import json
import requests
import threading
import jsonpickle
from urllib.parse import urlparse, unquote_plus, quote_plus
import random
import xmltodict, json
from rembg import remove



import sys, os, errno
import re
import signal
import math

#Internal Imports
from app import app, db, turbo
from app.forms import LoginForm, RegistrationForm
from app.models import User
import time




@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()






###
# Routes
###

@app.route('/')
@app.route('/index')
def index():
    

    return render_template('index.html', title='Home')

