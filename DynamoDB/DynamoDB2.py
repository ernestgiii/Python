# This table creates our initial DynamoDB table
import boto3

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='GOATMovies',
        KeySchema=[
            {
                'AttributeName':'year',
                'KeyType':'HASH'
            },

            {
                'AttributeName':'movietitles',
                'KeyType':'RANGE'
            }
        ],

        AttributeDefinitions=[
            {
                'AttributeName':'year',
                'AttributeType':'N'
            },
            {
                'AttributeName':'movietitles',
                'AttributeType':'S'  
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits':10,
            'WriteCapacityUnits':10
        }


    )

    return table

if __name__ == "__main__":
    movie_table = create_movie_table()
    print("Table status : ", movie_table.table_status)