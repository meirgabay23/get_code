
No idea how to hide the SECRET and KEY
Possible solution- I probably need to use the ".env" file, it will contain a dictionary with those variables
Solution- storing all credentials in my_credentials.py file, and then importing this file when needed

Connection refused when used 127.0.0.1:5000
Changed Gunicorn to run on 0.0.0.0 and it works! :)