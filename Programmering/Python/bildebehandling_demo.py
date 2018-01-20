from scipy.misc import imread
import matplotlib.pyplot as plt

img = imread('houses.jpg',flatten=True)

print(img.shape)
plt.imshow(img,cmap='gray')
plt.show()
