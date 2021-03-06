from fileinput import filename
from flask import Flask, request, Response, session
from request_handler import handle_check_user, handle_getDevice_info, handle_validate_input, handle_read_latest, handle_read_history
from server_configuration.configure import configure_app
import logging
import json
app = Flask(__name__)
configure_app(app)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.get("/home")
def do_gethome():

    app.logger.info("IP %s", request.remote_addr)
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

@app.get("/deviceInfo")
def do_getDevInfo():

    app.logger.info("IP %s", request.remote_addr)
    #Check if user loggedin
    if "logIn" in session:
        if(not handle_getDevice_info()):
            response = Response ("Note found", status = 404, mimetype='application/text')
        else:
            response = Response (handle_getDevice_info(), status = 200, mimetype = 'application/json')
    else:
        response = Response ("Unautherized", status = 401, mimetype='application/text')
    return (response)

@app.get("/state/history")
def do_getStateHistory():

    app.logger.info("IP %s", request.remote_addr)

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
    
    app.logger.info("IP %s", request.remote_addr)

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

    app.logger.info("IP %s", request.remote_addr)

    if "logIn" in session:
        session.pop("logIn",None)
        response = Response ("Ok", status = 200, mimetype = 'application/text')
    else:
         response = Response ("Unautherized", status = 401, mimetype='application/text')
    return response

@app.post('/login')
def do_login():

    app.logger.info("IP %s", request.remote_addr)

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
