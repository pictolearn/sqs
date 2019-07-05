# List all queues
# https://queue.amazonaws.com/716927497993/Picto-Test
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# List SQS queues
response = sqs.list_queues()

print(response['QueueUrls'])
