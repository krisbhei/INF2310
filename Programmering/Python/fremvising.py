from scipy.misc import imread
import matplotlib.pyplot as plt

img = imread("houses.png",flatten=True) # flatten=True gjør et fargebilde til gråtonebilde

plt.imshow(img)
plt.title("Et gråtonebilde?")

plt.figure() # For å lage et nytt vindu

plt.imshow(img,cmap='gray')
plt.title("Et gråtonebilde")

plt.show() # Husk dette for å faktisk se visualiseringene!
