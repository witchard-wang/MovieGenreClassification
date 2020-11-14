import pandas as pd
import tmdbsimple as tmdb
import shutil
import urllib.request
import requests
import json
import csv
import numpy as np
import string
import os

#gets movie based on ID
#@param ID int, id of movie from tmdb
#@param count int, tracks current movie poster 
#@returns title, filename, genre, and whether poster exists
def getMovie(ID, count):
    tmdbv3 = '9bc7e5ee4b6c54454c8b6f0fadf4a1cf'
    tmdb.API_KEY = tmdbv3
    movie = tmdb.Movies(ID)
    response = movie.info()
    image = False
    # for i in response.keys():
    #     print(i)
    folderpath = "posters"
    try:
        os.mkdir(folderpath)
    except OSError:
        print ("Directory %s already exists" % folderpath)
    else:
        print ("Successfully created the directory %s " % folderpath)

    filename = "posters/movie" + str(count) + ".png"
    title = "\"" + response['title'] + "\""
    genreJSON = response['genres']
    genres = []
    for x in genreJSON:
        genres.append(x['name'])
    #print(title)
    #print(response['poster_path'])
    #print(genres)
    lang = response['original_language']
    date = response['release_date']
    #print(lang)
    #print(date)
    if not (response['poster_path'] == None or len(genres) == 0): 
        image_path = 'https://image.tmdb.org/t/p/original' + response['poster_path']
        r = requests.get(image_path, stream = True)
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
            image = True
            #print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')
        print(image_path)

        # urllib.request.urlretrieve(image_path, filename)
    print()
    return title, filename, ' '.join(map(str, genres)), image, lang, date

#reads and saves movie posters into poster folder
#saves movie information into a csv file
def readIDs(total):
    with open('movie_ids_11_12_2020.json', encoding='utf-8') as rawJSON:
        with open('mov_IDs.csv','w', encoding="utf-8") as movFile:
            #read all possible movie ids and randomize
            lines = rawJSON.readlines()
            mov_IDs = []
            for x in lines:
                mov_IDs.append(json.loads(x)['id'])
            mov_IDs = np.random.permutation(mov_IDs)

            #save movie information 
            fields = ['Title', 'Genres', 'Poster_Path', 'Language', 'Release_Date']
            writer = csv.DictWriter(movFile, fieldnames=fields,lineterminator = '\n')
            writer.writeheader()            
            count = 0
            idx = 0           
            while count < total:
                mov = mov_IDs[idx]
                t, f, g, p, l, d = getMovie(mov, count)
                if p == True:
                    writer.writerow({'Title': t, 'Genres': g, 'Poster_Path': f, 'Language' : l, 'Release_Date' : d})
                    count += 1
                    
                idx += 1


# print(response['title'])
# print(response['poster_path'])
# print(response['genres'])
# image_path = 'https://image.tmdb.org/t/p/original' + response['poster_path']
# print(image_path)
# filename = response['title']
# r = requests.get(image_path, stream = True)
# # Check if the image was retrieved successfully
# if r.status_code == 200:
#     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#     r.raw.decode_content = True
    
#     # Open a local file with wb ( write binary ) permission.
#     with open(filename,'wb') as f:
#         shutil.copyfileobj(r.raw, f)
        
#     print('Image sucessfully Downloaded: ',filename)
# else:
#     print('Image Couldn\'t be retreived')

               
readIDs(5000)