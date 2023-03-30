# This script demostrates how to add additonal items to DynamoDB 

import boto3

db = boto3.resource('dynamodb')

table = db.Table('WWE')

with table.batch_writer() as batch:
    batch.put_item(
        Item = {
            'Wrestler':'Randy Orton',
            'SignatureMove':'RKO'
        }
    )

    batch.put_item(
        Item = {
            'Wrestler':'Shawn Michaels',
            'SignatureMove':'Sweet Chin Music'
        }
    )

    batch.put_item(
        Item = {
            'Wrestler':'Roman Reigns',
            'SignatureMove':'Spear'
        }
    )

    batch.put_item(
        Item = {
            'Wrestler':'Stone Cold',
            'SignatureMove':'Stunner'
        }
    )