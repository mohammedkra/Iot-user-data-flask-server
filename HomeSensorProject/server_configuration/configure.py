from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from key_handling.session_key_handling import read_session_PrivKey

def configure_app(app):

    #Retrieve the application's private key
    session_secretKey = read_session_PrivKey()

    #Configure the application to use the private key
    app.config['SECRET_KEY'] = session_secretKey

    #Configure the application to use db.sqlite3 for storing sessions
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    db = SQLAlchemy(app)
    app.config['SESSION_SQLALCHEMY'] = db

    #Initiate a server session
    server_sessions = Session()
    server_sessions.init_app(app)