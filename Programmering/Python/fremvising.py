from scipy.misc import imread
import matplotlib.pyplot as plt

img = imread("houses.png",flatten=True)

plt.imshow(img,cmap='gray')
plt.title("En tittel")

plt.show() # Husk dette for å faktisk se visualiseringene!
