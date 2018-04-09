import numpy as np
from numpy.fft import fft2,ifft2,fftshift
import matplotlib.pyplot as plt
from scipy.misc import imread
from basisbilder import *

# a
img = imread('car.png',flatten=True)

img_fft = fft2(img)
img_angle = np.arctan2(np.real(img_fft),np.imag(img_fft))

plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.log(np.abs(img_fft) + 1),cmap='gray',aspect='auto')
plt.title('Fourier spekter')

plt.subplot(1,2,2)
plt.imshow(img_angle*180/np.pi,cmap='gray',aspect='auto')
plt.title('Fase')

# b
img_dc = img_fft[0,0]
img_sum = np.sum(img)

print("img[0,0] = %g"%abs(img_dc)) # Merk at img_fft er kompleks.
                                   # Det gjør at det kommer en advarsel i terminalen
                                   # ved kjøring av programmet.
                                   # Imaginærdel skal være 0 (eller såpass lite at det tilnærmes lik 0).
                                   # Kan bruke abs for å fjerne advarsel.
print("sum(img) = %g\n"%img_sum)

# c
u,v = 5,7
N = img.shape[0] # siden vi får vite at bildet er kvadratisk

# lage sinus-bilde:
sin_img = lag_basis(u,v,N,N)

# plott resultatene:
plt.figure()

plt.subplot(3,1,1)
plt.imshow(sin_img,cmap='gray',aspect='auto')
plt.title('Sinus med frekvens (u,v) = (%d,%d)'%(u,v))
plt.xlabel('v'); plt.ylabel('u')

plt.subplot(3,1,2)
plt.title('Bildet langs horisontal akse')
plt.plot(sin_img[0,:])

plt.subplot(3,1,3)
plt.title('Bildet langs vertikal akse')
plt.plot(sin_img[:,0])

# d
img_mult = np.sum(img*sin_img)
print("sum(img*sin_img) = %g"%img_mult)
print("imag(F(5,7)) = %g\n"%np.imag(img_fft[u,v]))

# e

# lage cosinus-bilde:
cos_img = lag_basis(u,v,N,N,False)

img_mult = np.sum(img*cos_img)
print("sum(img*cos_img) = %g"%img_mult)
print("real(F(5,7)) = %g"%np.real(img_fft[u,v]))

plt.show()
