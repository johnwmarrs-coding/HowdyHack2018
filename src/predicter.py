import numpy as np

from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pickle
import os

color_names=["BLACK", "BLUE","?", "GREEN", "?", "?", "ORANGE","?", "WHITE", "RED", "YELLOW"]


model = load_model('color_classifier_massive.h5')

def get_color(r,g,b):
	result = model.predict(np.array([[r, g, b]]))
	result_array = result[0].tolist()
	return color_names[result_array.index(max(result_array))]

