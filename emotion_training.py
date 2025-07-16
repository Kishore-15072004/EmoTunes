from keras.utils import to_categorical
from keras_preprocessing.image import load_img
from keras.models import Sequential
from keras.layers import Dense, Conv2D,Dropout, Flatten, MaxPooling2D
import os
import pandas as pd
import numpy as np
TRAIN_DIRECTORY = "images/train"
TEST_DIRECTORY = "images/validation"
def createDataFrame(dir):
    image_paths=[]
    labels=[]
    for label in os.listdir(dir):
        for imageName in os.listdir(os.path.join(dir,label)):
            image_paths.append(os.path.join(dir,label,imageName))
            labels.append(label)
        print(label,"completed")
    return image_paths,labels
train = pd.DataFrame()
train['image'],train['label']=createDataFrame(TRAIN_DIRECTORY)
print(train)
test = pd.DataFrame()
test['image'],test['label']=createDataFrame(TEST_DIRECTORY)
print(test)
from tqdm import tqdm  # Use the standard tqdm

def extract_features(images):
    features = []
    for image in tqdm(images):
        img = load_img(image, color_mode="grayscale")
        img = np.array(img)
        features.append(img)
    features = np.array(features)
    features = features.reshape(len(features), 48, 48, 1)
    return features

# Your existing code...
train_features = extract_features(train['image'])
test_features = extract_features(test['image'])

print(train_features.shape)
x_train=train_features/255.0
x_test=test_features/255.0
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(train['label'])
y_train=le.transform(train['label'])
y_test=le.transform(test['label'])
y_train=to_categorical(y_train,num_classes=7)
y_test=to_categorical(y_test,num_classes=7)
import keras
model=Sequential()
# Define the input layer
input_layer = keras.Input(shape=(48, 48, 1))

# Create the Sequential model with the input layer
model = keras.Sequential([input_layer])

#convolutional layers
model.add(Conv2D(128,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0,4))

model.add(Conv2D(256,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0,4))

model.add(Conv2D(512,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0,4))

model.add(Conv2D(512,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Dropout(0,4))

model.add(Flatten())

#fully connected layers
model.add(Dense(512,activation='relu'))
model.add(Dropout(0,4))
model.add(Dense(256,activation='relu'))
model.add(Dropout(0,3))

#output layer
model.add(Dense(7,activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x=x_train,y=y_train,batch_size=128,epochs=100,validation_data=(x_test,y_test))
model_json=model.to_json()
with open("emotiondetector01.json",'w') as json_file:
    json_file.write(model_json)
model.save("emotiondetector01.h5")