from load_cifar import *
download_extract()
imagearray, labelarray = load_batch()   #   200 train   50 test     3 is cat id 
x_train, y_train, x_test, y_test = train_test(imagearray, labelarray, 200, 50, 3)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
model = Sequential()
model.add(Dense(units=64, activation='relu', input_shape=(3072,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=20, batch_size=128, verbose=1)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
print('Test loss:', loss_and_metrics[0])
print('Test accuracy:', loss_and_metrics[1])

model.save('cifar.h5')