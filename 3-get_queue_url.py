# Get Queue URL
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Get URL for SQS queue
response = sqs.get_queue_url(QueueName='Picto-Test')

print(response['QueueUrl'])