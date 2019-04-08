import json
import os
import boto3 

from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

DYNAMODB_TABLE = os.environ['table_name']


def lambda_handler(event, context):
    print(json.dumps(event))
    http_method = event.get('httpMethod')
    if (http_method == 'POST'):
        save(event)
        return {
            "statusCode": 200,
            "body": "Hi 4Developers"
                }
    else:
        return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "Hello 4Developers"}
        ),
    }

@xray_recorder.capture('dynamodb')
def save(event):
    request_id = event['requestContext']['requestId']
    body = event['body']
    payload = json.loads(body)
    name = payload['name']
    subsegment = xray_recorder.begin_subsegment('saving_user')
    subsegment.put_annotation('name', name)
    xray_recorder.end_subsegment()
    client = boto3.client('dynamodb')
    response = client.put_item(
        TableName = DYNAMODB_TABLE,
        Item = {
            'id': {'S':request_id},
            'name': {'S':name}
        }
    )


