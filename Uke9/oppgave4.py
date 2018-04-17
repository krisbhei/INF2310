import numpy as np
from numpy.fft import fft2,ifft2,fftshift
import matplotlib.pyplot as plt
from scipy.misc import imread

img = imread('forresampling.png',flatten=True)

for d in range(1,5):
    img_d = img[::d] # hente ut verdier med d mellomrom
    img_d_fft = fft2(img_d)

    plt.figure()

    plt.subplot(1,2,1)
    plt.imshow(img_d,cmap='gray',aspect='auto')
    plt.title('Bildet nedsamplet med d = %d steg'%d)

    plt.subplot(1,2,2)
    plt.imshow(np.log(np.abs(fftshift(img_d_fft))+1),cmap='gray',aspect='auto')
    plt.title('Fourier-spekter til bilde nedsamplet med d = %d'%d)

plt.show()
