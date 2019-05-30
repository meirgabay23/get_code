
# Use an official Python runtime as a parent image
FROM python:3.7-slim
LABEL  Meir Gabay

# Create the directory /code
RUN mkdir /code

# Copy the current directory contents into the container at /code
COPY . /code

# Set the working directory to /code
WORKDIR /code

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set the working directory to /code
RUN python manage.py migrate