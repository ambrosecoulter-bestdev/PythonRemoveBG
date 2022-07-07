#External Imports
from keyword import kwlist
from flask import render_template, flash, redirect, url_for, request, jsonify, send_file
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
from rembg import remove, bg
from PIL import Image
import glob
import numpy as np






import sys, os, errno
import re
import signal
import math

#Internal Imports
from app import app, db, turbo
from app.forms import LoginForm, RegistrationForm
from app.models import User
import time

from app.interference import remove_background




@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()




basedir = os.path.abspath(os.path.dirname(__file__))

###
# Routes
###

@app.route('/<filename>')
@app.route('/index')
def index(filename):
    input_path = 'app/static/'+filename
    output_path = os.path.join(basedir, 'static/output/output'+str(random.randint(0,100))+'.png')

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, alpha_matting=True)
            o.write(output)

    return send_file(output_path, mimetype='image/png')




@app.route('/testpixel')
def testpixel():

    directory = os.fsencode('app/static/mask_input')
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
    
        im = Image.open('app/static/mask_input/'+filename)
        im = im.convert('RGBA')

        data = np.array(im)   # "data" is a height x width x 4 numpy array
        red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

        other = (alpha != 0)
        data[..., :-1][other.T] = (255, 255, 255) # Transpose back needed

        # Replace white with red... (leaves alpha values alone...)
        transparent = (red == 0) & (blue == 0) & (green == 0) & (alpha == 0)
        data[...][transparent.T] = (0, 0, 0,255) # Transpose back needed

        

        im2 = Image.fromarray(data)
        im2.save(os.path.join(basedir, 'static/mask_output/output_'+filename), "PNG")
    return('Completed')
