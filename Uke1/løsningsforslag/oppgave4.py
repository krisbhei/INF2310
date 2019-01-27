from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

f = imread('mona.png',as_gray=True)

for ii in range(1,8,2):
    bit = ii

    quantized = f//2**(8-bit) # Operasjonen // betyr at vi gjør heltallsdivisjon.

    plt.figure() # lag nytt vindu
    plt.title("bit = %d, antall verdier = %d"%(bit, np.max(quantized) + 1))
    plt.imshow(quantized,cmap='gray')

plt.show()
