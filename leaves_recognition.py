# -*- coding: utf-8 -*-

"""
Created on Tue Nov 26 13:22:52 2019

@author: Habibullah
"""

import os
import zipfile
import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile
import matplotlib.pyplot as plt

local_zip = 'leaf_uci.zip'
zip_ref = zipfile.ZipFile(local_zip,'r')
zip_ref.extractall("C:/Users/Habibullah/Desktop/Leaves Recognition")
zip_ref.close()


liste = ["Quercus suber","Salix atrocinerea","Populus nigra","Alnus sp","Quercus robur",
         "Crataegus monogyna","Ilex aquifolium","Nerium oleander","Betula pubescens",
         "Tilia tomentosa","Acer palmaturu","Celtis sp","Corylus avellana","Castanea sativa",
         "Populus alba","Acer negundo","Taxus bacatta","Papaver sp","Polypodium vulgare",
         "Pinus sp","Fraxinus sp","Primula vulgaris","Erodium sp","Bougainvillea sp",
         "Arisarum vulgare","Euonymus japonicus","Ilex perado ssp azorica","Magnolia soulangeana",
         "Buxus sempervirens","Urtica dioica","Podocarpus sp","Acca sellowiana","Hydrangea sp",
         "Pseudosasa japonica","Magnolia grandiflora","Geranium sp","Aesculus californica",
         "Chelidonium majus","Schinus terebinthifolius","Fragaria vesca"]
         

try :
    os.mkdir("C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/training")
    os.mkdir("C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/testing")

except OSError :
    pass

for variety in liste :
    try :
        os.mkdir("C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/training/" + variety)
        os.mkdir("C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/testing/" + variety)
    except OSError :
        pass

#Örnek 2 klasör görüntüleyelim.
 
#print(len(os.listdir("C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/training/Acer negundo")))
#print(len(os.listdir("C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/testing/Acer palmatum")))
    
def split_data(SOURCE, TRAINING,TESTING,SPLIT_SIZE) :
    files = []
    for filename in os.listdir(SOURCE) :
        file = SOURCE + filename
        if os.path.getsize(file) > 0 :
            files.append(filename)
        else :
            print(filename + "is zero length, so ignoring")

    training_length = int(len(files) * SPLIT_SIZE)
    testing_length = int(len(files) - training_length)
    shuffled_set = random.sample(files,len(files))
    training_set = shuffled_set[0:training_length]
    testing_set = shuffled_set[-testing_length:]
    
    for filename in training_set :
        this_file = SOURCE + filename
        destination = TRAINING + filename
        copyfile(this_file,destination)
    
    for filename in testing_set :
        this_file = SOURCE + filename
        destination = TESTING + filename
        copyfile(this_file,destination)

split_size = .8

for name in liste :
    SOURCE_DIR = "C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/" + name + "/"
    TRAINING_DIR = "C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/training/" + name + "/"
    TESTING_DIR = "C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/testing/" + name + "/"
    
    split_data(SOURCE_DIR,TRAINING_DIR,TESTING_DIR,split_size)

TRAINING_DIR = "C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/training/"
training_datagen = ImageDataGenerator(rescale = 1./255)

training_generator = training_datagen.flow_from_directory(
        TRAINING_DIR,
        target_size = (300,300),
        class_mode = "categorical")

TESTING_DIR = "C:/Users/Habibullah/Desktop/Leaves Recognition/leaf_uci/testing/"
testing_datagen = ImageDataGenerator(rescale = 1./255)

testing_generator = testing_datagen.flow_from_directory(
        TESTING_DIR,
        target_size = (300,300),
        class_mode = "categorical")


model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3,3), activation = "relu", input_shape = (300,300,3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation = "relu"),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(128, (3,3), activation = "relu"),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(128, (3,3), activation = "relu"),
        tf.keras.layers.MaxPooling2D(2,2),
        
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1024, activation = "relu"),
        tf.keras.layers.Dense(40, activation = "softmax")
        ])
    
model.summary()

model.compile(loss = "categorical_crossentropy", optimizer = RMSprop(lr=0.001), metrics = ['accuracy'])

history = model.fit_generator(training_generator,
                              epochs = 50,
                              validation_data = testing_generator,
                              verbose = 1)

acc=history.history['acc']
val_acc=history.history['val_acc']
loss=history.history['loss']
val_loss=history.history['val_loss']

epochs=range(len(acc))

plt.plot(epochs, acc, 'r', "Training Accuracy")
plt.plot(epochs, val_acc, 'b', "Validation Accuracy")
plt.title('Training and validation accuracy')
plt.figure()

plt.plot(epochs, loss, 'r', "Training Loss")
plt.plot(epochs, val_loss, 'b', "Validation Loss")
plt.figure()







    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
     
