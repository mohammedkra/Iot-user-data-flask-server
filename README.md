# Iot-user-data-flask-server
This project is a flask web server with pre registered users who can login and fetch som Iot based data stored on the server
The project is divided into different packets, each packet is responsible for a specific function in the server
The flask web server project contains some secure features such as:
A certified https running web server
Check if user is logged in before accessing data using sessions
A good way of logging user activities (this is presented inside server.py file)
An antidos attack script (this feature is presented in the antidos.sh script file)
User passwords are stored using becrypt (example in the check_login folder)
Input validation "against improper data entering the server" (example in the login_request_validation folder)
