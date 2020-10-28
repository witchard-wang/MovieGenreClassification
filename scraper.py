import requests
import pandas as pd
import tmdbsimple as tmdb

tmdbv3 = '9bc7e5ee4b6c54454c8b6f0fadf4a1cf'

tmdb.API_KEY = tmdbv3
movie = tmdb.Movies(123452)
response = movie.info()

for i in response.keys():
    print(i)

print(response['title'])
print(response['poster_path'])
print(response['genres'])
image_path = 'https://image.tmdb.org/t/p/original' + response['poster_path']
print(image_path)