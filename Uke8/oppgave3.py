import numpy as np
from numpy.fft import fft2,ifft2,fftshift
import matplotlib.pyplot as plt
from scipy.misc import imread

img = imread('car.png',flatten=True)

img_fft = fft2(img)

thr = 1
for i in range(1,7):
    img_thr = img_fft.copy()
    img_thr[np.abs(img_fft) < thr] = 0
    img_recon = ifft2(img_thr)

    plt.figure()

    plt.subplot(1,3,1)
    plt.imshow(np.log(np.abs(img_thr)+1),cmap='gray',aspect='auto')
    plt.title('Bevarte koeffsienter: %g %%'%(np.sum(img_thr != 0)/img.size*100))

    plt.subplot(1,3,2)
    plt.imshow(np.abs(img_recon),cmap='gray',aspect='auto')
    plt.title('Rekonstruert bilde ved terskel: %d'%thr)

    plt.subplot(1,3,3)
    plt.imshow(img,cmap='gray',aspect='auto')
    plt.title('Originalbilde')

    thr *= 10

plt.show()
