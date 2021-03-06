"""Import & Setup CIFAR Dataset"""

from tensorflow.python.keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# preprocessing
x_train = x_train.astype('float32') # for division
x_test = x_test.astype('float32')
x_train /= 255 # normalise
x_test /= 255

from tensorflow.python.keras.utils import to_categorical
# One-hot encode the labels
num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

"""Define Model"""

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, Activation, MaxPooling2D, Dropout, Flatten, Dense 

model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', input_shape=x_train.shape[1:]))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

"""Create / Restore Checkpoint"""

from tensorflow.python.keras.models import load_model
from keras.callbacks import ModelCheckpoint

filepath='checkpoint.h5'
checkpoint = ModelCheckpoint(filepath, verbose=1, save_best_only=True)

import os.path
if os.path.exists(filepath): model = load_model(filepath)

"""Train Model"""

model.summary()

model.fit(x_train, y_train, batch_size=32,
          validation_data=(x_test, y_test),
          callbacks=[checkpoint],
          epochs=10)

scores = model.evaluate(x_test, y_test, verbose=1)
print('Test accuracy:', scores[1]) #  0.7437

"""To clear model memory run model definition"""
