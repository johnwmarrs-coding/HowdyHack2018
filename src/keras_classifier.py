import numpy as np

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pickle
import os

#Loading the data set
color_names=["black", "green", "blue", "brown", "purple", "maroon", "red", "pink", "orange", "yellow", "mustard"]


data = np.load('color_names.npz')

samples = data['samples']
labels = data['labels']

label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(labels)
#print(integer_encoded)

onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

print(onehot_encoded)
print(len(onehot_encoded[0]))

model = Sequential()

model.add(Dense(250, input_dim=3, activation='relu' ))
model.add(Dense(200, activation='relu'))
model.add(Dense(11, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])



model.fit(samples, onehot_encoded, epochs=15, batch_size=10)

#scores = model.evaluate()
result = model.predict(np.array([[255, 0, 0]]))

result_array = result[0].tolist()
max_index = result_array.index(max(result_array))
print(color_names[max_index])


model.save('color_classifier_massive.h5')






