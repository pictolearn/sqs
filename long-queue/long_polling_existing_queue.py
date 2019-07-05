# long_polling_existing_queue.py demonstrates how to set the default number of seconds to wait between retrieving a message.

import boto3

# Assign this value to an existing queue URL before running the program
queue_url = 'SQS_QUEUE_URL'

# Enable long polling on the queue
sqs = boto3.client('sqs')
sqs.set_queue_attributes(QueueUrl=queue_url,
                         Attributes={'ReceiveMessageWaitTimeSeconds': '20'})