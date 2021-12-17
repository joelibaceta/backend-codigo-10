from tensorflow import keras
import numpy as np

from PIL import Image

fashion_mnist = keras.datasets.fashion_mnist

saved_model = keras.models.load_model('../fashion_mnist_model.h5')

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()



i_input=np.array([test_images[255]])


predictions = saved_model.predict(i_input)

print(np.argmax(predictions[0]))