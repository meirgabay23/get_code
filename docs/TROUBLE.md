
No idea how to hide the SECRET and KEY
Possible solution- I probably need to use the ".env" file, it will contain a dictionary with those variables
Solution- storing all credentials in my_credentials.py file, and then importing this file when needed

Connection refused when used 127.0.0.1:5000
Changed Gunicorn to run on 0.0.0.0 and it works! :)

How to connect to DynamoDB with Python using hidden credentials?
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html

Adding reigon_name to client variable
https://stackoverflow.com/questions/40377662/boto3-client-noregionerror-you-must-specify-a-region-error-only-sometimes