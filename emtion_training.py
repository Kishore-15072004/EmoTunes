import os
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras_preprocessing.image import load_img
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.utils import class_weight
import tensorflow as tf

# Enable eager execution
tf.config.experimental_run_functions_eagerly(True)

# Directories
TRAIN_DIRECTORY = "images/train"
TEST_DIRECTORY = "images/test"
VISUALIZATION_DIRECTORY = "visualizations"

def createDataFrame(dir):
    image_paths = []
    labels = []
    for label in os.listdir(dir):
        for imageName in os.listdir(os.path.join(dir, label)):
            image_paths.append(os.path.join(dir, label, imageName))
            labels.append(label)
    return image_paths, labels

# Create DataFrames
train = pd.DataFrame()
train['image'], train['label'] = createDataFrame(TRAIN_DIRECTORY)
test = pd.DataFrame()
test['image'], test['label'] = createDataFrame(TEST_DIRECTORY)

# Extract features
def extract_features(images):
    features = []
    for image in images:
        img = load_img(image, color_mode="grayscale")
        img = np.array(img)
        features.append(img)
    features = np.array(features)
    features = features.reshape(len(features), 48, 48, 1)
    return features

# Prepare data
train_features = extract_features(train['image'])
test_features = extract_features(test['image'])
x_train = train_features / 255.0
x_test = test_features / 255.0

# Encode labels
le = LabelEncoder()
le.fit(train['label'])
y_train = le.transform(train['label'])
y_test = le.transform(test['label'])
y_train = to_categorical(y_train, num_classes=7)
y_test = to_categorical(y_test, num_classes=7)

# Calculate class weights to handle imbalanced data
class_weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(train['label']),
    y=train['label']
)
class_weights = dict(enumerate(class_weights))

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True
)
datagen.fit(x_train)

# Build model
model = Sequential([
    Conv2D(128, (3, 3), activation='relu', input_shape=(48, 48, 1)),
    MaxPooling2D(2, 2),
    Dropout(0.4),
    Conv2D(256, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Dropout(0.4),
    Conv2D(512, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Dropout(0.4),
    Conv2D(512, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Dropout(0.4),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.4),
    Dense(256, activation='relu'),
    Dropout(0.3),
    Dense(7, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Enable detailed logging for debugging
tf.debugging.set_log_device_placement(True)

# Try running without data generator to debug
try:
    history = model.fit(
        x_train, y_train,
        batch_size=128,
        epochs=100,
        validation_data=(x_test, y_test),
        class_weight=class_weights
    )
except Exception as e:
    print(f"Error during training without generator: {e}")
    history = model.fit(
        datagen.flow(x_train, y_train, batch_size=128),
        epochs=100,
        validation_data=(x_test, y_test),
        class_weight=class_weights
    )

# Save model
model_json = model.to_json()
with open("emotiondetector01.json", 'w') as json_file:
    json_file.write(model_json)
model.save("emotiondetector01.h5")

# Ensure visualization directory exists
if not os.path.exists(VISUALIZATION_DIRECTORY):
    os.makedirs(VISUALIZATION_DIRECTORY)

# Plotting training history
def plot_training_history(history):
    # Plot training & validation accuracy values
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.savefig(os.path.join(VISUALIZATION_DIRECTORY, 'accuracy.png'))

    # Plot training & validation loss values
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.savefig(os.path.join(VISUALIZATION_DIRECTORY, 'loss.png'))

    plt.tight_layout()
    plt.show()

# Visualize training history
plot_training_history(history)
