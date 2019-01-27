from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

filename = 'mona.png'
f = imread(filename,as_gray=True)

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
plt.title("med bias, uten endring av kontrast")
plt.imshow(f_out + bias,cmap='gray',vmin=0,vmax=255)

plt.figure()
plt.title("med bias, med endring av kontrast")
plt.imshow(f_out*1.5 + bias,cmap='gray',vmin=0,vmax=255)

# Bilde uten bias . trenger strengt tatt ikke dette da matplotlib kan tilpasse seg bildets verdier
plt.figure()
plt.title("uten bias, uten endring av kontrast")
plt.imshow(f_out, cmap='gray')

# For å kunne se at vi gjør en kontrastendring, kan vi spesifisere i matplotlib at
# vi ønsker å fremvise bildet innenfor f_out sine verdiers range til sammenligning.
# Hvis vi ikke hadde gjort dette, ville matplotlib mappet gråtone instensitetene
# i forhold til det konstrastendrete bildet sine verdier, og derav ville vi ikke kunne se noen endring.
plt.figure()
plt.title("uten bias, med endring av kontrast")
plt.imshow(f_out*1.5,cmap='gray',vmin=np.min(f_out), vmax=np.max(f_out))

plt.show()
