import requests
import pandas as pd
import tmdbsimple as tmdb
import shutil

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
filename = response['title']
r = requests.get(image_path, stream = True)
# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')