from datetime import datetime

from flask import render_template, request, flash, redirect, url_for, jsonify, session
from flask_login import current_user, login_user, logout_user, login_required

from app import app, models, db
from app.forms import LoginForm, RegistrationForm


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


#@app.route('/play_game', methods=['GET'])
#def play_game():
#    return render_template('game.html')

@app.route('/restart', methods=['GET'])
def restart():
    return render_template('game.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/_add_high_score', methods=['POST'])
def _add_high_score():
    if current_user.is_authenticated:
        distance = request.json['distance']
        mountains = request.json['mountains']
        user = current_user.username
        high_score = models.HighScore()
        high_score.update_user_record(user, distance, mountains)
        db.session.add(high_score)
        db.session.commit()
    return 'success', 200


@app.route('/high_score', methods=['GET'])
def high_score():
    result = models.HighScore.query.with_entities(models.HighScore.username,
                                                  models.HighScore.distanceWalked,
                                                  models.HighScore.mountainsClimbed).order_by(models.HighScore.distanceWalked.desc()).limit(5).all()
    return render_template('high_score.html', data=result)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You are now logged out')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

