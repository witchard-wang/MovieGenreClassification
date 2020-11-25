import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model
from tensorflow.keras.models import save_model



#Folder specification
folder = "posters"

# formatting image dimensions
img_width = 350
img_height = 350
img_count = len([item for item in os.listdir('posters') if os.path.isfile(os.path.join('posters', item))])

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
def setupData():
    data = pd.read_csv("mov_IDs.csv")
    i = -1  
    for genres in data['Genres']:
        i = i + 1
        genres = genres.split()
        for genre in genres:
            if genre not in data.columns:
                data[genre] = [0 for a in range(0,img_count)]
            data.iloc[i, data.columns.get_loc(genre)] = 1
    print(data)

    dataModel = data.drop(['Popularity', 'ID','Title', 'Genres', 'Poster_Path', 'Release_Date', 'Language'], axis = 1)
    # dataModel = dataModel.drop(dataModel.index[10:5000])
    print(dataModel)
    dataModel = dataModel.to_numpy()
    img_array = processImages(folder)
    return data, dataModel, img_array

def setupNeuralNetwork(dataModel, img_array):
    X_train, X_test, y_train, y_test = train_test_split(img_array, dataModel, random_state = 0, test_size = 0.15)
    print(X_train.shape)

    #Build sequential CNN
    model = Sequential()

    #Configure convolutional layers, specify filter and activation function
    model.add(Conv2D(16, (3,3), activation='relu', input_shape = X_train[0].shape))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.3))

    model.add(Conv2D(32, (3,3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.3))

    model.add(Conv2D(64, (3,3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.4))

    model.add(Conv2D(128, (3,3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2,2))
    model.add(Dropout(0.5))

    model.add(Flatten())

    model.add(Dense(128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))


    model.add(Dense(128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))


    model.add(Dense(len(data.columns) - 7, activation='sigmoid'))
    print(model.summary())
    #print("train:", X_train.shape)
    #print("test:", X_test.shape)

    # Compile and fit the model. Validation data is the data used to evaluate the accuracy of our model
    model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])
    history = model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
    plot_learningCurve(history, 5)
    return model


def plot_learningCurve(history, epoch):
  # Plot training & validation accuracy values
  epoch_range = range(1, epoch+1)
  plt.plot(epoch_range, history.history['accuracy'])
  plt.plot(epoch_range, history.history['val_accuracy'])
  plt.title('Model accuracy')
  plt.ylabel('Accuracy')
  plt.xlabel('Epoch')
  plt.legend(['Train', 'Val'], loc='upper left')
  plt.show()

  # Plot training & validation loss values
  plt.plot(epoch_range, history.history['loss'])
  plt.plot(epoch_range, history.history['val_loss'])
  plt.title('Model loss')
  plt.ylabel('Loss')
  plt.xlabel('Epoch')
  plt.legend(['Train', 'Val'], loc='upper left')
  plt.show()


def predictGenre(model, img):
    # load weights into new model
    print("Loaded model from disk")
    img = image.load_img(img, target_size = (img_width, img_height, 3))
    plt.imshow(img)
    img = image.img_to_array(img)
    img = img/255.0
    img = img.reshape(1, img_width, img_height, 3)

    genres = data.columns[7:]
    #print(genres)
    probGenres = model.predict(img)
    #print(probGenres[0])
    #print(np.argsort(probGenres[0]))
    top3Genres = np.argsort(probGenres[0])[:-4:-1]
    #print(probGenres[0][top3Genres])

    for i in range(3):
            print(genres[top3Genres[i]])
    return genres[top3Genres]


sampleImg = (folder + "/movie") + str(170) + ".png" 
data, dataModel, img_array = setupData()
#model = setupNeuralNetwork(dataModel, img_array)
#model.save("savedModel")
loaded_model = load_model("savedModel")
print("Loaded model from disk")
predictGenre(loaded_model, sampleImg)