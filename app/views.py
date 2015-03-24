# -*- coding: utf-8 -*-
import os
from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, login_manager
from database import db_session
from forms import RegistrationForm, MoneyMarketForm, LoginForm
from app.models import User, MoneyChanger
import flask_login as login
import datetime



@app.route('/')
@app.route('/index/')
def index():
    form = LoginForm()
    return render_template("index.html", form = form)



@login_manager.user_loader
def load_user(id):
    return db_session.query(User).get(id)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form_r = RegistrationForm()
    form = LoginForm()
    if form_r.validate_on_submit() and form_r.validate_r():
        user = User(username = form_r.username.data, email = form_r.email.data, password = form_r.password.data)
        db_session.add(user)
        db_session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('register.html', form_r = form_r, form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit() and form.get_user():
            user = form.get_user()
            if user is None :
                error = 'Invalid username or password.'
            else:  
                login_user(user)
                flash('Welcome ' + user.email, 'success')
                return redirect(url_for("index"))
    return render_template('login.html', form = form, error = error)
    #no flash in message error

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))





@app.route('/money', methods=['GET', 'POST'])
def money():
    form = MoneyMarketForm(request.form)
    if form.validate_on_submit():
        money = MoneyChanger(want = form.want.data, 
                            currency = form.currency.data, 
                            total = form.total.data, 
                            course = form.course.data, 
                            phone = form.phone.data, 
                            city = form.city.data, 
                            area = form.area.data, 
                            comment = form.comment.data, 
                            relevant = form.relevant.data,
                            pub_date = form.pub_date.data
                            )
        db_session.add(money)
        db_session.commit()
        flash("Goodluck change money")
        return redirect(url_for('index'))
    return render_template('money.html', form = form)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


'''@app.route('/money/', methods=['GET', 'POST'])
def money():
    form = MoneyMarketForm(request.form)
    return render_template('money.html', form = form)


def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Welcome ' + user.email, 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form = form)




    @app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'GET':
        user = User(form.username.data, form.email.data, form.password.data)
       # db.session.add(user)
        #db.session.commit()
        flash('Thanks for registered')
        return redirect(url_for('login'))




app.route('/money', methods=['GET', 'POST'])
def money():
    form = MoneyMarketForm(request.form)
    if form == 'POST' and form.validate():
        money = MoneyChanger(form.want.data,form.currency.data, form.total.data, form.course.data, 
                            form.phone.data, form.city.data, form.area.data, 
                            form.comment.data, form.relevant.data)
        db_session.add(money)
        db_session.commit()
        flash("Goodluck change money")
        return redirect(url_for('index'))
    return render_template('money.html', form = form)
    '''
