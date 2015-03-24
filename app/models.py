# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Date
from database import Base
import datetime
from sqlalchemy.orm import relationship
import database
from wtforms.fields import DateField
#from flask.ext.login import UserMixin
#import flask.ext.whooshalchemy as whooshalchemy


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(32))
    #passwordc = Column(String(32))

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return unicode(self.id)

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
        

    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


class MoneyChanger(Base):
    __tablename__ = 'moneychanger'

    id = Column(Integer, primary_key=True)
    want = Column(String)
    currency = Column(String)
    total = Column(String)
    course = Column(Integer)
    phone = Column(String)
    city = Column(String)
    area = Column(String)
    comment = Column(String)
    relevant = Column(Integer)
    pub_date = Column(Date, nullable=False)

    def __init__(self,currency,want,total,course,phone,city,area,comment,relevant,pub_date):
        self.want = want
        currency = currency
        self.total = total
        self.course = course
        self.phone = phone
        self.city = city
        self.area = area
        self.comment = comment
        self.relevant = relevant
        self.pub_date = pub_date

