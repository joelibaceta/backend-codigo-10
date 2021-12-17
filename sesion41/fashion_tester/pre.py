from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

im = mpimg.imread('sneaker_test.jpg')#.convert('L')
#imr = im.resize((28, 28))

gray = rgb2gray(im)

plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show(

)