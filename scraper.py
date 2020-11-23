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
  try:
    tmdbv3 = '9bc7e5ee4b6c54454c8b6f0fadf4a1cf'
    tmdb.API_KEY = tmdbv3
    
    movie = tmdb.Movies(ID)
    response = movie.info()
    image = False
    # for i in response.keys():
    #     print(response[i])
    folderpath = "posters"
    # try:
    #     os.mkdir(folderpath)
    # except OSError:
    #     print ("Directory %s already exists" % folderpath)
    # else:
    #     print ("Successfully created the directory %s " % folderpath)

    filename = "posters/movie" + str(count) + ".png"
    title = "\"" + response['title'] + "\""
    genreJSON = response['genres']
    genres = []

    for x in genreJSON:
      genres.append(x['name'])
    print(title)
    print(response['poster_path'])
    print(genres)
    lang = response['original_language']
    date = response['release_date']
    pop = response['popularity']
    print(lang)
    if date == "":
      date = "-100"
    print(date)
    print(pop)
    if not (response['poster_path'] == None or len(genres) == 0) and (int(date[0:4]) >= 2000) and lang == "en":  
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
        print('Image sucessfully Downloaded: ',filename)
      else:
        print('Image Couldn\'t be retreived')
      print(image_path)

        # urllib.request.urlretrieve(image_path, filename)
    return title, filename, genres, image, lang, date, pop
  except Exception:
    print('failed')
    return 'x', 'x', 'x', False, 'x', 'x','x'

#reads and saves movie posters into poster folder
#saves movie information into a csv file
def readIDs(total):
  with open('movie_ids_11_23_2020.json', encoding='utf-8') as rawJSON:
      with open('mov_IDs.csv','w', encoding="utf-8") as movFile:
        #read all possible movie ids and randomize
        lines = rawJSON.readlines()
        mov_IDs = []
        genres = {"Animation" : 0, "Comedy" : 0, "Thriller" : 0, "Horror" : 0, "Drama" : 0, "Documentary" : 0, "Music" : 0,
              "Family" : 0, "TV Movie" : 0, "Adventure" : 0, "Fantasy" : 0, "Science Fiction" : 0, "Action" : 0,
              "Crime" : 0, "Romance" : 0, "Mystery" : 0, "History" : 0, "Western" : 0, "War" : 0}
        for x in lines:
          mov_IDs.append(json.loads(x)['id'])
        mov_IDs = np.random.permutation(mov_IDs)

        #save movie information 
        fields = ['Title', 'Genres', 'Poster_Path', 'Language', 'Release_Date', 'Popularity', 'ID']
        writer = csv.DictWriter(movFile, fieldnames=fields,lineterminator = '\n')
        writer.writeheader()            
        count = 0
        idx = 0           
        while count < total:
          mov = mov_IDs[idx]
          t, f, g, p, l, d, pop = getMovie(mov, count)
          cap_gen = False
          if type(g) != type(str()):
            for gen in g:
              if genres[gen] > 700:
                cap_gen = True
            
            
            if p == True and not cap_gen:
              for gen in g:
                genres[gen] += 1
              print(genres)
              mov_gen = ' '.join(map(str, g))
              writer.writerow({'Title': t, 'Genres': mov_gen, 'Poster_Path': f, 'Language' : l, 'Release_Date' : d, 'Popularity' : pop, 'ID' : mov})
              count += 1  
          print(idx, total-count)
          print() 
          idx += 1

readIDs(5000)