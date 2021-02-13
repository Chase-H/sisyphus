from datetime import datetime

from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import current_user, login_user, logout_user, login_required

from app import app


@app.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@app.route('/game', methods=['GET'])
def play_game():
    return render_template('game.html')
