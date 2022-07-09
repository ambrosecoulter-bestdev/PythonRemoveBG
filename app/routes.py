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

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', basedir1=basedir)










###INFERENCE API

###INFERENCE W ALPHA MATTING PREPROCESS
@app.route('/am-inference', methods=['GET', 'POST'])
def am_inference():
    if request.method == 'POST':
        #Upload image
        image = request.files.get('file')
        image.save(os.path.join(basedir, 'static/input-uploaded/', image.filename))
        
        input_path = os.path.join(basedir, 'static/input-uploaded/', image.filename)
        output_path = os.path.join(basedir, 'static/output/', image.filename)

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input, alpha_matting=True)
                o.write(output)

        return ('static/output/' + image.filename)


###INFERENCE W/O ALPHA MATTING PREPROCESS
@app.route('/noam-inference', methods=['GET', 'POST'])
def noam_inference():
    if request.method == 'POST':
        #Upload image
        image = request.files.get('file')
        image.save(os.path.join(basedir, 'static/input-uploaded/', image.filename))
        
        input_path = os.path.join(basedir, 'static/input-uploaded/', image.filename)
        output_path = os.path.join(basedir, 'static/output/', image.filename)

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input, alpha_matting=False)
                o.write(output)

        return ('static/output/' + image.filename)
###











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
        im2.convert('RGB')
        im2.save(os.path.join(basedir, 'static/mask_output/output_'+filename), "PNG")
    return('Completed')
