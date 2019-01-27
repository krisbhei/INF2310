from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np

f = imread('mona.png',flatten=True)


noiseFactor = 10
N,M = f.shape
fNoisy = f + noiseFactor*np.random.randn(N,M)

for ii in range(1,8,2):
    bit = ii
    quantized = f//2**(8-bit)

    plt.figure()
    plt.title("bit = %d, antall verdier = %d"%(bit, np.max(quantized)+1))
    plt.imshow(quantized,cmap='gray')

plt.show()
