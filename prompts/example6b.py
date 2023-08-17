import boto3

# Create SES client
ses = boto3.client('ses', region_name='us-east-1')

#function to verify email address