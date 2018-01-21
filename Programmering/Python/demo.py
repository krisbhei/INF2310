from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np

img = imread("houses.png",flatten=True)

plt.imshow(img,cmap='gray')
plt.title("Originalbilde")

# Øke kontrast
img_increased_contrast = img*1.5

# Gjøre bildet lysere
img_brighter = img + 100

plt.figure()

plt.subplot(2,1,1) # subplot deler et vindu i flere delplott.
plt.imshow(img_increased_contrast,cmap='gray',vmin=0,vmax=255,aspect='auto')
plt.title("Økt kontrast")

plt.subplot(2,1,2)
plt.imshow(img_brighter,cmap='gray',vmin=0,vmax=255,aspect='auto')
plt.title("Økt lyshet")

plt.show()
