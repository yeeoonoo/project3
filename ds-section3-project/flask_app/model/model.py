from flask import Blueprint
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

bp = Blueprint('model', __name__, url_prefix='/model')

@bp.route('/', methods=['POST', 'GET'])
def values():
    return render_template('values.html')
