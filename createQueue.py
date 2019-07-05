# Demonstrates how to create a queue
import boto3

# Create SQS client
# Note , make sure that the $ aws configure command is run and the access key id is set.
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='Picto-Test',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)


# In your system, always store the entire queue URL exactly as Amazon SQS returns it 
# to you when you create the queue (for example, https://sqs.us-east-2.amazonaws.com/123456789012/MyQueue). 
# Don't build the queue URL from its separate components each time you need to specify the queue URL in a request
# because Amazon SQS can change the components that make up the queue URL.
print(response['QueueUrl'])
 
