import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.preprocessing import image

# formatting image dimensions
img_width = 350
img_height = 350
img_count = len([item for item in os.listdir('posters') if os.path.isfile(os.path.join('posters', item))])
print(img_count)

# Formats each image present in folder, and adds them to an array.
def processImages(folder):
    img_array = []

    i = 0
    while i < img_count:
        filename = (folder + "/movie") + str(i) + ".png"
        img = image.load_img(filename, target_size = (img_width, img_height, 3))
        img = image.img_to_array(img) # Converting the image to an array
        img = img / 255.0 # Converting to neural network preferred values
        img_array.append(img)
        i = i + 1
    img_array = np.array(img_array)
    return img_array


#Creates CNN to classify images
def setupNeuralNetwork():
    data = pd.read_csv("mov_IDs.csv")
    i = -1
    for genres in data['Genres']:
        i = i + 1
        genres = genres.split()
        for genre in genres:
            if genre not in data.columns:
                data[genre] = [0 for i in range(0,img_count)]
            data.iloc[i, data.columns.get_loc(genre)] = 1
    #print(data)

    dataModel = data.drop(['Title', 'Genres', 'Poster_Path'], axis = 1)
    dataModel = dataModel.to_numpy()
    #print(dataModel)

    # training and testing model
    X_train, X_test, y_train, y_test = train_test_split(img_array, dataModel, random_state = 0, test_size = 0.1)

    #Build sequential CNN
    


    
setupNeuralNetwork()
processImages("posters")