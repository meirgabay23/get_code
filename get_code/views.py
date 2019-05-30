from django.shortcuts import render
from django.http import HttpResponse
import os
import json

# Create your views here.
def index(request):
    import boto3
    from boto3.dynamodb.conditions import Key
    client = boto3.client(
        'dynamodb',
        aws_access_key_id=os.environ['AWS_KEY'],
        aws_secret_access_key=os.environ['AWS_SECRET'],
        region_name=os.environ['AWS_REGION']
    )

    MyKey = {
        os.environ['AWS_TABLE_KEY']: {
            'S': os.environ['CODE_NAME'],
        }
    }

    response = client.get_item(
        TableName=os.environ['AWS_TABLE_NAME'],
        Key=MyKey
    )

    response = json.dumps(response["Item"])
    item = json.loads(response)
    item = item[os.environ['AWS_RETURN_KEY_VALUE']][os.environ['AWS_RETURN_KEY_TYPE']]
    msg = f"{{ {os.environ['AWS_RETURN_KEY_VALUE']}: {item} }}"
    return HttpResponse(msg)
