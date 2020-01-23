from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

f = imread('mona.png',as_gray=True)


noiseFactor = 10
N,M = f.shape
fNoisy = f + noiseFactor*np.random.randn(N,M)

# Nå kan fNoisy ha verdier over og under [0,255].
# Det er mulig å transformere fNoisy  slik at minste og største verdi til fNoisy
# blir henholdsvis 0 og 255.
# Transformasjonen kommer vi tilbake til senere i emnet:
fNoisy = (fNoisy - np.min(fNoisy)) / (np.max(fNoisy)- np.min(fNoisy)) * 255

# Merk at i denne oppgaven er det viktigste at du får til at bildet
# kan ha opp til 2**bit antall verdier

for ii in range(1,8,2):
    bit = ii
    quantized = f//2**(8-bit)

    plt.figure()
    plt.title("bit = %d, antall mulige verdier = %d"%(bit, np.max(quantized)+1))
    plt.imshow(quantized,cmap='gray')

plt.show()
