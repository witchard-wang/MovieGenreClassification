# CSCE 320 Project - Cinemaniacs (Classification of Movie Genre based on Movie Poster)
Aniruddha Srinivasan
Vidhur Potluri
Richard Wang

# Our Final Results are located in "Final Deliverable.ipynb"
Movie posters can be designed in a confusing way even for humans. We wanted to create a model that is able to predict the movie genre of a movie poster. 

Our primary goal is to create a working prediction model to predict the genre of movie that a movie is based primarily on the poster only. Our secondary goal was to look at features of movie posters and see whether there are any patterns that emerge from them. The features that this study looked at was the dominant color of the movie poster and if it had a face on the poster, the emotion that the faces had. 


### Note - Running the "Final Deliverable.ipynb" can take hours to run.

Movie data obtained using The Movie Database(TMDB) API through the tmdbsimple python wrapper module. It is limited to download and scrape movie posters from movies that were made for an english speaking audience after the year 2000 and we limited the max number of movies that can come from a specific genre to 700 movies. This means that if there after the 700th Drama movie is scraped it will stop getting more movies. The movie posters are located in the 'posters' folder and the descriptive data is located in mov_ids.csv. If you want to get a new dataset, you can run the scraper.py file only after you get your own api key

### Dependencies
In order to run scraper must add tmdbsimple to python environment
`pip install tmdbsimple`

Extracting colors from image. Used when running the "Final Deliverable.ipynb" 
`pip install colorthief`

Image resizing using OpenCV. Used when running the "Final Deliverable.ipynb" 
`pip install opencv-python`

In order to run imageClassification and the neural network, must add tensorflow to python environment. Used when running the "Final Deliverable.ipynb" 
 `pip install tensorflow`.
You need to configure tensorflow to your system's requirements to have the prediction model working properly.

### Note - If you would like to make predictions on your own posters, you would have to run setupData() first (section 1.1). This could take up to 10 minutes. Then run predictGenre with your image as an argument as shown in the final analysis section of the notebook (Part 3).


  

