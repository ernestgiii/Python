import boto3 
import json
from decimal import Decimal 

def load_movie(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('GOATMovies')

    for movie in movies: 
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie: ", year, title)
        item = {
            'year': year,
            'movietitles': title,
            'info': movie['info']
        }
        table.put_item(Item=item)


if __name__=="__main__":
    with open('moviedata.json') as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)

    load_movie(movie_list)
