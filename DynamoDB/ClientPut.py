import boto3 

db = boto3.client('dynamodb')


response = db.put_item(
    TableName='WWE', 

    Item = {
    'Wrestler': {
        'S':'Undertaker'
    },
    'SignatureMove' : {
        'S':'Chokeslam'
    }
    }
)