# Demonstrates how to designate 
import json

import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/716927497993/Picto-Test'
dead_letter_queue_arn = 'arn:aws:sqs:us-east-1:716927497993:DLQ'

redrive_policy = {
    'deadLetterTargetArn': dead_letter_queue_arn,
    'maxReceiveCount': '10'
}


# Configure queue to send messages to dead letter queue
sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'RedrivePolicy': json.dumps(redrive_policy)
    }
)
 