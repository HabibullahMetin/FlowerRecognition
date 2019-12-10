# -*- coding: utf-8 -*-

"""
Created on Tue Dec 09 13:52:52 2019

@author: Yusuf
"""

import os
import zipfile
import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile
import matplotlib.pyplot as plt
from keras.preprocessing import image
from tensorflow import lite
import numpy as np
from google.colab import files
uploaded = files.upload()
from google.colab import files
 
        
local_zip = '17flowers.zip'
zip_ref = zipfile.ZipFile(local_zip,'r')
zip_ref.extractall("C:/Users/Yusuf/Desktop/Leaves Recognition")
zip_ref.close()


liste =  ["daffodil", "snowdrop", "lilyvalley", "bluebell", "crocus",
			   	   "iris", "tigerlily", "tulip", "fritillary", "sunflower", 
			       "daisy", "coltsfoot", "dandelion", "cowslip", "buttercup",
			       "windflower", "pansy","sword","dieffenbachia","calatheas"]
         

try :
    os.mkdir("C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/training")
    os.mkdir("C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/testing")

except OSError :
    pass

for variety in liste :
    try :
        os.mkdir("C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/training/" + variety)
        os.mkdir("C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/testing/" + variety)
    except OSError :
        pass

# Örnek 2 klasör görüntüleyelim.
 
# print(len(os.listdir("C:/Users/Habibullah/Desktop/Leaves Recognition/flower_photos/training/Acer negundo")))
# print(len(os.listdir("C:/Users/Habibullah/Desktop/Leaves Recognition/flower_photos/testing/Acer palmatum")))
 
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
    SOURCE_DIR = "C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/" + name + "/"
    TRAINING_DIR = "C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/training/" + name + "/"
    TESTING_DIR = "C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/testing/" + name + "/"
    
    split_data(SOURCE_DIR,TRAINING_DIR,TESTING_DIR,split_size)

TRAINING_DIR = "C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/training/"
training_datagen = ImageDataGenerator(rescale = 1./255,
                    rotation_range=45,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    horizontal_flip=True,
                    shear_range=0.2,
                    zoom_range=0.2,
                    fill_mode='nearest'
                    )

training_generator = training_datagen.flow_from_directory(
        TRAINING_DIR,
        
        target_size = (300,300),
        class_mode = "categorical")

TESTING_DIR = "C:/Users/Yusuf/Desktop/Leaves Recognition/flowers/testing/"
testing_datagen = ImageDataGenerator(rescale = 1./255
                  )

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
        tf.keras.layers.Conv2D(128, (3,3), activation = "relu"),
        tf.keras.layers.MaxPooling2D(2,2),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1024, activation = "relu"),
        tf.keras.layers.Dense(20, activation = "softmax")
        ])
    
model.summary()

model.compile(loss = "categorical_crossentropy", optimizer = RMSprop(lr=0.001), metrics = ['accuracy'])

# model.load_weights("mnist-model4.h5")

# path='C:/Users/Yusuf/Desktop/indir.jpg'
# img=image.load_img(path,target_size=(300,300))
# x=image.img_to_array(img)
# x=np.expand_dims(x, axis=0)
# images = np.vstack([x])
# sonuc = model.predict(images, batch_size=10)
# print(sonuc[0])
# print(np.argmax(sonuc))
# a=np.argmax(sonuc)
# print(a)
# if a==0:
#    print("it is a bluebell")
# if a==1:
#    print("it is a buttercup")
# if a==2:
#    print("it is a calatheas")
# if a==3:
#    print("it is a coltsfoot")
# if a==4:
#    print("it is a cowslip")
# if a==5:
#    print("it is a crocus")
# if a==6:
#    print("it is a daffodil")
# if a==7:
#    print("it is a daisy")
# if a==8:
#    print("it is a dandelion")
# if a==9:
#    print("it is a dieffenbachia")
# if a==10:
#    print("it is a fritiallary")
# if a==11:
#    print("it is a iris")
# if a==12:
#    print("it is a lilyvalley")
# if a==13:
#    print("it is a pansy")
# if a==14:
#    print("it is a snowdrop")
# if a==15:
#    print("it is a sunflower")
# if a==16:
#    print("it is a sword")
# if a==17:
#    print("it is a tigerlily")
# if a==18:
#    print("it is a tulip")
# if a==19:
#    print("it is a windflower")    


history = model.fit_generator(training_generator,
                          epochs = 20,
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

keras_file="mnist-model7.h5"
model.save(keras_file)
converter=lite.TocoConverter.from_keras_model_file(keras_file)
tflite_model=converter.convert()
open("linear.tflite7","wb").write(tflite_model)
files.download('mnist-model7.h5')
files.download('7linear.tflite')

