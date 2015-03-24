# -*- coding: utf-8 -*-
from flask import flash
from werkzeug import secure_filename
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, validators,\
                    SubmitField, SelectField, IntegerField, StringField, DateTimeField
from wtforms.validators import Required, EqualTo, Email, Regexp, NumberRange
#from wtforms.ext.csrf.session import SessionSecureForm
from database import db_session
from app.models import User
from datetime import datetime
from wtforms.fields import DateTimeField


want_choice = ['buy', 'sell']

class RegistrationForm(Form):
    username = StringField('Username', validators = [validators.Length(1, 64),
                                                    Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 
                                                    0,'Username must have only letteres,'
                                                    'numbers, dots or underscores')])
    email = StringField('Email Address', validators = [Required(), Email(), validators.Length(1, 64)])
    password = PasswordField('New Password',  validators = [validators.required()])
    #EqualTo('confirm', message='Passwords must match')]

    def validate_r(self):
        if db_session.query(User).filter_by(email=self.email.data).count() > 0:
            flash('Duplicate email', 'danger')
            return False
        if db_session.query(User).filter_by(username=self.username.data).count() > 0:
            flash('Duplicate username', 'danger')
            return False
        return True

class LoginForm(Form):
    email = TextField('email', validators = [Email(), validators.required(), validators.Length(1, 64)])
    password = PasswordField('password', validators = [validators.required()])


    def get_user(self):
        return db_session.query(User).filter_by(email=self.email.data, password=self.password.data).first()

'''
    def validate_login(self):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')'''

    #def get_user(self):
    #    return User.query.filter_by(email=self.email.data).first()

class MoneyMarketForm(Form):
    want = SelectField('State', choices=[('b', 'buy'), ('s', 'sell')])
    currency = SelectField('curency', choices=[('u','USD'),('e','EUR'),('r','RUB')])
    total = IntegerField('total', [validators.required()])
    course = IntegerField('course', [validators.required('Please enter your course')])
    phone = StringField('phone', validators = [validators.required(), Regexp('^\+?[0-9]{3}-?[0-9]{6,12}$')])
    city = SelectField('city' , choices=[('k','Kiev'),('C','Cherkassy'),('K','Kremenchuk'), ('Ch', 'Chernigof')])
    area = StringField('area', [validators.required(), validators.Length(max=200)])
    comment = StringField('cooment', [validators.required(), validators.Length(max=350)])
    relevant = IntegerField('relevant',[validators.required()])#?
    #submint = SubmitField('Send')
    pub_date = DateTimeField('Posted Date (mm/dd/yy)', validators=[Required()], format='%d/%m/%Y')
    #("date", format='%Y-%m-%d %H:%M:%S')

    #def get_money(self):
    #    return db_session.query(MoneyMarketForm).filter_by(city=self.city.data).first()

    


#language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
'''
def validate_login(self):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Duplicate email', 'danger')
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Duplicate name', 'danger')

'''