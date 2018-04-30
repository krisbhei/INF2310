import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from histogram_image import *
from numpy.fft import fft2,ifft2,fftshift

img = imread('discImage.png',flatten=True)
img_fft = fft2(img)

N,M = img.shape

h,ax = hist(img)

plt.figure()

for counter,n in enumerate([3,5,7,9]):
    f = np.ones((n,n))/(n*n)
    f_fft = fft2(f,(N,M))

    img_inv = ifft2(f_fft*img_fft)

    h_filtered = hist(np.round(np.real(img_inv)))[0]

    plt.subplot(2,2,counter+1)
    plt.plot(ax,h_filtered)
    plt.plot(ax,h)
    plt.legend(['filtrert','opprinnelig'])
    plt.title('Normaliserte histogram til opprinnelig bilde vs. bilde \n filtrert med %d x %d middelverdifilter'%(n,n))

plt.show()
