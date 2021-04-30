from flask import Blueprint, Flask, request, g, redirect, url_for, \
		  render_template, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3

# configuration
bp = Blueprint('review', __name__)

@bp.route('/')
def home():
	return render_template('review/home.html')

@bp.route('/about')
def about():
	return render_template('review/about.html')