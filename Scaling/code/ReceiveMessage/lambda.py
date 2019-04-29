import boto3
import time
import datetime
import uuid

client = boto3.client('sqs')
uuid = str(uuid.uuid4())

def lambda_handler(event, context):
    handle = event['Records'][0]['receiptHandle']
    time.sleep(0.5)
    print('Time: ' + str(datetime.datetime.now()) + ' Id: ' + uuid)
    '''
    response = client.delete_message(
        QueueUrl='https://sqs.eu-west-1.amazonaws.com/655379451354/4developers_queue',
        ReceiptHandle=handle
    )
    '''
