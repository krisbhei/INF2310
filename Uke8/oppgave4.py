import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from numpy.fft import fft2,ifft2,fftshift

img = imread('lena_periodicNoise.png',flatten=True)

# a
img_fft = fft2(img)

plt.figure()
plt.imshow(np.log(np.abs(img_fft) + 1),cmap='gray')
plt.title('Fourier spekter til lena_periodicNoise')

# b
N,M = img.shape

u1,v1 = 40,100
u2,v2 = 60,196

u1_,v1_ = N-u1,M-v1 # bruker her konjugert symmetri i bildet
u2_,v2_ = N-u2,M-v2

img_fft[[u1,u1_,u2,u2_],[v1,v1_,v2,v2_]] = 0
img_recon = np.abs(ifft2(img_fft))


plt.figure()

plt.subplot(1,3,1)
plt.imshow(np.log(np.abs(img_fft) + 1),cmap='gray',aspect='auto')
plt.title('Fourier spekter')

plt.subplot(1,3,2)
plt.imshow(img_recon,cmap='gray',aspect='auto')
plt.title('Rekonstruert bilde')

plt.subplot(1,3,3)
plt.imshow(img,cmap='gray',aspect='auto')
plt.title('Originalbilde - lena_periodicNoise')

# c
img = imread('lena_periodicNoise2.png',flatten=True)

N,M = img.shape

img_fft = fft2(img)


plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.log(np.abs(img_fft) + 1),cmap='gray')
plt.title('Fourier spekter til lena_periodicNoise2')

plt.subplot(1,2,2)
plt.imshow(img,cmap='gray')
plt.title('Originalbilde')

u,v = 40,100
u_,v_ = N-u,M-v

img_fft[[u,u_],[v,v_]] = 0


plt.figure()

plt.subplot(1,3,1)
plt.imshow(np.log(np.abs(img_fft) + 1),cmap='gray',aspect='auto')
plt.title('Fourier spekter')

plt.subplot(1,3,2)
plt.imshow(img_recon,cmap='gray',aspect='auto')
plt.title('Rekonstruert bilde')

plt.subplot(1,3,3)
plt.imshow(img,cmap='gray',aspect='auto')
plt.title('Originalbilde - lena_periodicNoise2')

plt.show()
