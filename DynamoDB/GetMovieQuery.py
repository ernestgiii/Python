import boto3 
from boto3.dynamodb.conditions import Key

def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    
    # This is the name of our table and the year 
    table = dynamodb.Table('GOATMovies')

    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )

    return response['Items']


# This queries our movies by the year 
if __name__ == '__main__':
    query_year=1979
    print("Movies from {}".format(query_year))

    movies = query_movies(query_year)

    for movie in movies:
        print(movie['year'], ":", movie['movietitles'])