# This script demostrates everything about the table 
import boto3 
from pprint import pprint 

db = boto3.client('dynamodb')


response = db.describe_table(
    TableName = 'WWE'
)

pprint(response) 
