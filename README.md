# dev-ops challenge - Meir Gabay

#### Technologies that I used ####

* Fetching a key value from DynamoDB - python boto3
* Building a container - Docker hosted in Dockerhub
* Testing the container - Travis


## Prerequisites

Have the following installed:

## Installation

Five installation steps

#### 1. Cloning repository to local machine

Create a folder anywhere on your machine, name it: *csod-project*

Open Command-Prompt (Terminal) in that *csod-project* folder and clone the project to local repository
```
C:\Users\my_user\Documents\csod-project\>git clone https://github.com/unfor19/csod-automation/
```

##### Current folder structure #####
```
C:\Users\my_user\Documents\csod-project\csod-automation\
```

#### 2. Creating a new Python virtual environment
Still in Command-Prompt (Terminal) in the same folder *csod-project*, create a new virtual environment.

The name of the folder will be: *ENV*

**Note**: The module *venv* comes out-of-the box with Python v3.6 and above.
```
C:\Users\my_user\Documents\csod-project\>python -m venv ENV
```

##### Current folder structure #####
```
C:\Users\my_user\Documents\csod-project\csod-automation\
C:\Users\my_user\Documents\csod-project\ENV\
```

#### 3. Activate virtual environment ####
Assuming we are currently in the *csod-project* folder, then:

```
C:\Users\my_user\Documents\csod-project>ENV\Scripts\activate
(ENV) C:\Users\my_user\Documents\csod-project>
```

#### 4. Install necessary requirements with pip ####

``` (ENV) C:\Users\my_user\Documents\csod-project>pip install -r requirements.txt ```

**Note**: The installed packages will be available only for the *ENV* virtual environment.

#### 5. Modify the constants in csod_CONSTANTS.py ####
```
# URL
MY_PORTAL_URL = "https://my-portal.csod.com"

# Credentials
MY_USERNAME = "admin"
MY_PASSWORD = "adminPassword"
```

## Getting Started

#### Activate virtual environment ####
Assuming we are currently in the *csod-project* folder, then:

```
C:\Users\my_user\Documents\csod-project>ENV\Scripts\activate
(ENV) C:\Users\my_user\Documents\csod-project>
```

#### Adjusting the code ####
// TODO
Adjust the code according to your needs by editing: csod_edit_lo.py

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - IDE
* [Python](https://www.python.org) - Programming language for automation
* [Selenium](https://www.seleniumhq.org/) - Browser automation framework
* JavaScript - Manipulating HTML objects

## Author

* **Meir Gabay** - *Owner*

## License

This project is licensed under the GPL v3.0 License - see the [LICENSE](LICENSE) file for details
