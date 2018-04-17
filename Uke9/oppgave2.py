import numpy as np
from numpy.fft import fft2,ifft2,fftshift,ifftshift

import matplotlib.pyplot as plt
from scipy.misc import imread

def H(D0,P=512,Q=512):
    H = np.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
            D = np.sqrt(((u-0.5*P)/(0.5*P))**2+((v-Q*0.5)/(Q*0.5))**2)
            if D <= D0:
                H[u,v] = 1
    return H
    # hvis man ønsker å gjøre alt på én linje:
    # return np.array([[0 if np.sqrt(((u-0.5*P)/(0.5*P))**2+((v-Q*0.5)/(Q*0.5))**2) > D0 else 1 for v in range(Q)] for u in range(P)])

# a
D0 = 0.2
H1 = H(D0)

plt.figure()
plt.imshow(H1,cmap='gray')
plt.title("Ideelt lavpassfilter med D0 = %g i frekvensdomenet"%D0)

# b og c
H1_idft = ifftshift(ifft2(fftshift(H1))) # fftshift i bildedomenet siden ifft antar DC i [0,0].
                                         # Shift så tilbake for presentering av resultatet.

plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.imag(H1_idft),cmap='gray',aspect='auto')
plt.title("Imaginærdel til ideelt lavpassfilter med D0 = %g i bildedomenet"%D0)
plt.colorbar()

plt.subplot(1,2,2)
plt.imshow(np.real(H1_idft),cmap='gray',aspect='auto')
plt.title("Realdel til ideelt lavpassfilter med D0 = %g i bildedomenet"%D0)
plt.colorbar()

# d
D0 = 0.4
H2 = H(D0)

H2_idft = ifftshift(ifft2(fftshift(H2))) # fftshift i bildedomenet siden ifft antar DC i [0,0].
                                         # Shift så tilbake for presentering av resultatet.

plt.figure()
plt.imshow(np.real(H2_idft),cmap='gray',aspect='auto')
plt.title("Realdel til ideelt lavpassfilter med D0 = %g i bildedomenet"%D0)
plt.colorbar()

# e
img = imread('car.png',flatten=True)

img_fft = fft2(img,[512,512])

img_H1 = ifft2(img_fft*fftshift(H1))
img_H2 = ifft2(img_fft*fftshift(H2))

# Fjern effekt av nullutviding:
[N,M] = img.shape
img_H1 = img_H1[:N,:M]
img_H2 = img_H2[:N,:M]

# Vis reusltatet etter filtrering
plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.real(img_H1),cmap='gray',aspect='auto')
plt.title('Bildet car.png filtrert med H1')

plt.subplot(1,2,2)
plt.imshow(np.real(img_H2),cmap='gray',aspect='auto')
plt.title('Bildet car.png filtrert med H2')

# f
img_hp_H1 = ifft2(img_fft*fftshift(1-H1))
img_hp_H2 = ifft2(img_fft*fftshift(1-H2))

# Fjern effekt av nullutviding:
[N,M] = img.shape
img_hp_H1 = img_hp_H1[:N,:M]
img_hp_H2 = img_hp_H2[:N,:M]

# Vis resultatet etter filtrering
plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.abs(img_hp_H1),cmap='gray',aspect='auto')
plt.title('Bildet car.png filtrert med 1-H1')

plt.subplot(1,2,2)
plt.imshow(np.abs(img_hp_H2),cmap='gray',aspect='auto')
plt.title('Bildet car.png filtrert med 1-H2')

# g
img_H1_add = img_hp_H1 + img_H1
img_H2_add = img_hp_H2 + img_H2

plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.abs(img_H1_add),cmap='gray',aspect='auto')
plt.title('H1_lavpass + H1_høypass')

plt.subplot(1,2,2)
plt.imshow(np.abs(img_H2_add),cmap='gray',aspect='auto')
plt.title('H2_lavpass + H2_høypass')

plt.show()
