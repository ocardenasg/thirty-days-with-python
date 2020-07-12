import requests
from pprint import pprint

base_api = 'https://api.themoviedb.org/3'
api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZTQyZGZlZDcyYThlMDUzZjU5Nzg1ZmRhNWY4NGE4YyIsInN1YiI6IjVlZTZmYjVhYWZhMWIwMDAyM2MwYWU1NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5HvDfSqH4eCnwHXxxPyND7lvGU6Z0gc-xVpCAOsV6_A'
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json;charset=utf-8'
}


movie_500 = requests.get(f'{base_api}/movie/500', headers=headers)
print(movie_500.status_code)

movies_of_2020 = requests.get(
    f'{base_api}/search/movie?year=2020&query=marvel', headers=headers)
print(movies_of_2020.status_code)
pprint(movies_of_2020.json())
