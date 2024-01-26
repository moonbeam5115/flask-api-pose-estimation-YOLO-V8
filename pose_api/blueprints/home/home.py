from typing import List
from flask import Flask, render_template, Blueprint
from pose_api import create_app

bp = Blueprint('home', __name__)

# Routes
@bp.route('/')
def home():
    wo_data=[]
    return render_template('base.html', wo_data=wo_data)


@bp.route('/test')
def test():
    return render_template('test.html')
