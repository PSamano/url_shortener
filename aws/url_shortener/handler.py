import json
import boto3
import random
import string
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_short_url(event, context):
    data = json.loads(event['body'])
    original_url = data['url']
    shortcode = generate_shortcode()

    item = {
        'shortcode': shortcode,
        'original_url': original_url
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response

def get_original_url(event, context):
    shortcode = event['pathParameters']['shortcode']

    result = table.get_item(
        Key={
            'shortcode': shortcode
        }
    )

    if 'Item' in result:
        item = result['Item']
        response = {
            "statusCode": 302,
            "headers": {
                "Location": item['original_url']
            }
        }
    else:
        response = {
            "statusCode": 404,
            "body": "Shortcode not found"
        }

    return response
