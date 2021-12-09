from flask import Flask, request, Response, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from exportKeys import readPrivKey
from request_handler import handle_check_user, handle_validate_input, handle_read_latest, handle_read_history
import json

app = Flask(__name__)

#Retrieve the application's private key
session_secretKey = readPrivKey()

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

@app.get("/home")
def do_gethome():

    #Check if user loggedin
    if "logIn" in session:

        #Check if the file reading succeeds
        if (not handle_read_latest('state.json')):
            response = Response ("Note found", status = 404, mimetype='application/text')
        else:
            response = Response (handle_read_latest('state.json'), status = 200, mimetype = 'application/json')
    else:
        response = Response ("Unautherized", status = 401, mimetype='application/text')
    return(response)

@app.get("/state/history")
def do_getStateHistory():

    #Check if user loggedin
    if "logIn" in session:

        #Check if the file reading succeeds
        if (not handle_read_history()):
            response = Response ("Not found", status = 404, mimetype='application/text')
        else:
            response = Response (handle_read_history(), status = 200, mimetype = 'application/json')
    else:
        response = Response ("Unautherized", status = 401, mimetype='application/text')
    return(response)


@app.get("/alarm/latest")
def do_get_alarm_latest():

    #Check if user loggedin
    if "logIn" in session:

        #Check if file reading succeeds
        if(not handle_read_latest('burglarAlarm.json')):
            response = Response ("Not found", status = 404, mimetype='application/text')
        else:
            response = Response (handle_read_latest('burglarAlarm.json'), status = 200, mimetype = 'application/json')
    else:
        response = Response ("Unautherized", status = 401, mimetype='application/text')
    return(response)

@app.get("/logout")
def do_logout():
    if "logIn" in session:
        session.pop("logIn",None)
        response = Response ("Ok", status = 200, mimetype = 'application/text')
    else:
         response = Response ("Unautherized", status = 401, mimetype='application/text')
    return response

@app.post('/login')
def do_login():
    params = json.loads(request.data)

    if handle_validate_input(params):
        if handle_check_user(params):
            session['logIn'] = "True"
            response = Response ("Succesfull Autherization", status = 201, mimetype='application/text')

        else:
            response = Response ("Unautherized", status = 401, mimetype='application/text')
    else:
        response = Response ("Invalid input", status = 2101, mimetype='application/text')
    return(response)

app.run('127.0.0.1',debug=True, threaded = True, ssl_context=('cert.pem', 'key.pem'))
