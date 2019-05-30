from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    import os, json
    import boto3
    client = boto3.client(
        'dynamodb',
        aws_access_key_id=os.environ['AWS_KEY'],
        aws_secret_access_key=os.environ['AWS_SECRET'],
        region_name=os.environ['AWS_REGION']
    )
    return HttpResponse("Hello, world. You're at the polls index.")
