# -*- coding: utf-8 -*-

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import app


engine = create_engine('sqlite:///' + 'app.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import app.models
    Base.metadata.create_all(bind=engine)


#In REPL[python] create app.db
#glyki
#zapystit server, ostanovit server, repl zapustit moget ostanovit
#inogda nygna perezagryzka Repl[python] i ostanovka servera
#from app.database import init_db
#init_db()
'''

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + app.config['DATABASE']
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
#engine = create_engine('sqlite:///D:/pythonproject/program/Sublime/flaskstart/app.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)

#engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
#engine = create_engine('sqlite:///:memory:', echo=True)
#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

#engine = create_engine('sqlite:///:memory:', echo=True)#соеденяемся с БД
#Base = declarative_base()

#session = sessionmaker(bind=engine)




#engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
#engine = create_engine('sqlite:///:memory:', echo=True)
#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


#Base = declarative_base()
#Base.query = db_session.query_property()
#session = sessionmaker(bind=engine)
'''