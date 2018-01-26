from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np

filename = 'mona.png'
f = imread(filename,flatten=True)

# N: antall rader i bildet (matrise), M: antall kolonner i bildet
N,M = f.shape

f_out = np.zeros((N,M))

# Sett første rad i ut-bildet lik første rad i originalbilde.
# Dette gjøres fordi for-loopen starter på i = 1.
f_out[0,:] = f[0,:]

# La i starte på 1 og ikke 0 fordi f[-1,j] vil gi differansen
# mellom første og siste rad i originalbildet.
# Det går også fint å la programmet ta differansen mellom første og siste rad - så
# lenge det var et bevisst valg.
for i in range(1,N):
    for j in range(M):
        f_out[i,j] = f[i,j] - f[i-1,j]

bias = 128 # brukt bare for fremvising av bildet 

plt.figure()
plt.imshow(f_out + bias,cmap='gray',vmin=0,vmax=255)

plt.figure()
plt.imshow(f_out*1.5 + bias,cmap='gray',vmin=0,vmax=255)

plt.show()
