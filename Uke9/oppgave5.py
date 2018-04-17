import numpy as np
from numpy.fft import fft2,ifft2,fftshift
import matplotlib.pyplot as plt
from scipy.misc import imread

# Lager 2D vindue med størrelse win_size[0] x win_size[1]:
def tukeywin(win_size,alpha):

    h = np.zeros((2,max(win_size)))

    for i in range(2):
        sz = win_size[i]

        n1 = int(round(alpha*(sz-1)*0.5))
        n1_coor = np.arange(n1) # til å regne ut verdiene til cosinus-ene

        n2 = int(round((sz-1)*(1-alpha*0.5)))

        n3_coor = np.arange(n2,N)

        h[i,:n1] = 0.5*(1 + np.cos(np.pi*(2*n1_coor/(alpha*(sz-1)) - 1)))
        h[i,n1:n2] = 1
        h[i,n2:] = 0.5*(1 + np.cos(np.pi*(2*n3_coor/(alpha*(sz-1)) - 2/alpha + 1)))

    return np.outer(h[0],h[1])


img = imread('lena.png',flatten=True)
N = img.shape[0]

w = tukeywin(img.shape,0.5)
img_w = img*w

img_fft = fftshift(fft2(img))
img_w_fft = fftshift(fft2(img_w))

plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.log(np.abs(img_fft) + 1),cmap='gray')
plt.title("Spekter til bildet uten vindu")

plt.subplot(1,2,2)
plt.imshow(np.log(np.abs(img_w_fft)+1),cmap='gray')
plt.title("Spekter til bildet med vindu")

plt.show()
