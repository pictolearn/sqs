# demonstrates how to create a queue with a default 20 second to wait between retrieving messages. 
# This will reduce the number of empty responses returned and thus your bill.

import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue with long polling enabled
response = sqs.create_queue(
    QueueName='SQS_QUEUE_NAME',
    Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
)

print(response['QueueUrl'])
 