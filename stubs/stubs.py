import boto3

sqs = boto3.client('sqs')

response = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/YOUR_QUEUE_NAME',
    MessageBody='Hello, World!',
)

print(response)






# poetry add 'boto3-stubs' 'boto3-stubs[sqs]'
# from mypy_boto3_sqs.client import SQSClient