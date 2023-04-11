# This script updates your DynamoDB table 
import boto3

db = boto3.client('dynamodb')

response = db.update_table(
    TableName='WWE',
    BillingMode='PROVISIONED',

    ProvisionedThroughput={
        'ReadCapacityUnits':1,
        'WriteCapacityUnits':1
    }
)

print(response)