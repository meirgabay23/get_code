
Had to use this guide to run Docker while having VirtualBox - I'm using VirtualBox for my Python course
https://nickjanetakis.com/blog/docker-tip-13-get-docker-for-windows-and-virtualbox-working-together

Learn Docker
https://docs.docker.com/get-started/

Learning about gitignore patterns
https://www.atlassian.com/git/tutorials/saving-changes/gitignore

How did I get the secret_code ?
aws-cli DynamoDB command
https://stackoverflow.com/questions/34668367/how-to-return-items-in-a-dynamodb-on-aws-cli
https://docs.aws.amazon.com/cli/latest/reference/dynamodb/get-item.html (first example)

Python and DynamoDB - Read an Item
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html#GettingStarted.Python.03.02

Docker Compose - using "up"
https://docs.docker.com/compose/reference/up/

Boto3 get_item()
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html?highlight=dynamodb#DynamoDB.Client.get_item

Writing tests on response
https://stackoverflow.com/questions/11885211/how-to-write-a-unit-test-for-a-django-view
https://docs.djangoproject.com/en/2.2/topics/testing/overview/
https://stackoverflow.com/questions/40313230/python-unit-test-for-a-function-that-has-try-except


###
Suddenly I found this beautiful blog for developing Django app in Docker
https://blog.devartis.com/django-development-with-docker-a-completed-development-cycle-7322ad8ba508
https://blog.devartis.com/

Same blog- how to test the Django app in Docker
django-development-with-docker-testing-continuous-integration-and-docker-hub-57038ca19773
###

Running tests - Django and Docker container - overkill
https://howchoo.com/g/y2y1mtkznda/getting-started-with-docker-compose-and-django

Travis with Django - running tests
https://medium.com/@MicroPyramid/set-up-travis-ci-for-django-project-427d6dd2f46c

Downloading Ruby so I can run Travis CI on my machine
I need it for encrypting the .env variables
https://rubyinstaller.org/downloads/

Run in PowerShell
gem install travis
https://github.com/dwyl/learn-travis
https://github.com/travis-ci/travis.rb#encrypt

travis login --pro
login to travis ... only then the encryption will work

encrypt the my_credentials.py file
travis encrypt-file .\mysite\my_credentials.py -add
https://docs.travis-ci.com/user/encrypting-files/

Gave up on encrypting a file on Windows 10
Running same command on my Kali Linux VM
travis login --pro
travis encrypt-file mysite/my_credentials.py mysite/my_credentials.py.enc --add -r unfor19/get_code

Copied the my_credentials.py.enc from Linux Kali to my Google drive account
Downloaded the my_credentials.py.enc file from Google drive account to my Windows
Copied the contents of the travis.yml file K and IV, added "-md sha256" to the travis.yml

WORKS! Encrypted on openSSL 1.1 and decrypted on Travis's openSSL 1.0.2g
https://stackoverflow.com/questions/39637388/encryption-decryption-doesnt-work-well-between-two-different-openssl-versions/39641378#39641378


Created two environement variables in Travis, DOCKER_USERNAME and DOCKER_PASSWORD
https://docs.travis-ci.com/user/docker/#pushing-a-docker-image-to-a-registry

Added a deployment code
https://cinhtau.net/2016/09/02/use-travis-ci-in-github-to-build-and-deploy-to-dockerhub/


Travis didn't sync with Github so Omer recommended Drone.io
I used the following drone.yml and tweaked it
https://www.imagescape.com/blog/2017/04/28/continuous-integration-and-deployment-drone-docker-django-gunicorn-and-nginx-part-2/

Install scoop, so you can install drone (1.1.1)
https://0-8-0.docs.drone.io/cli-installation/
https://scoop.sh/
Powershell: 
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
scoop install drone


Authenticate with drone
https://0-8-0.docs.drone.io/cli-authentication/

