from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np

f = imread('lena.png',flatten=True)

bit = 2

quantized = f//2**(8-bit)

plt.imshow(quantized,cmap='gray',vmin=0,vmax=2**bit)
plt.show()
