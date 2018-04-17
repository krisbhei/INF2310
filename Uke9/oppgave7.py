import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from numpy.fft import fft2,ifft2,fftshift
from functools import reduce

img = imread('tekna133.png',flatten=True)
N,M = img.shape

def notch_filter(D0,n,zero_freq,P=512,Q=512):
    num_zero_freq = zero_freq.shape[0]

    H = np.zeros((P,Q))
    n2 = n*2
    for u in range(P):
        for v in range(Q):
            D = np.sqrt(((u-zero_freq[:,0])/(0.5*P))**2+((v-zero_freq[:,1])/(Q*0.5))**2)
            # Reduce med (lambda x,y: x*y) ganger hvert element i D .
            H[u,v] = reduce((lambda x,y: x*y),1-(1/(1+(D/D0)**(n2))))

    return H

# a
img_fft = fft2(img)
img_fft_pad = fft2(img,(2*N,2*M))

plt.figure()

plt.subplot(1,2,1)
plt.imshow(np.log(np.abs(img_fft) + 1),cmap='gray')
plt.title('Fourier til bilde u/padding')

plt.subplot(1,2,2)
plt.imshow(np.log(np.abs(img_fft_pad) + 1),cmap='gray')
plt.title('Fourier til bilde med padding')

# b

u1,v1 = 72,26
u1_,v1_= N-u1,M-v1 # utnytter konjugert symmetri

u2,v2 = 25,148
u2_,v2_ = N-u2,M-v2

u3,v3 = 174,74
u3_,v3_ = N-u3,M-v3

u4,v4 = 216,74
u4_,v4_ = N-u4,M-v4

u1_pad,v1_pad = u1*2,v1*2
u1_pad_,v1_pad_= 2*N-u1_pad,2*M-v1_pad # utnytter konjugert symmetri

u2_pad,v2_pad = u2*2,v2*2
u2_pad_,v2_pad_ = 2*N-u2_pad,2*M-v2_pad

u3_pad,v3_pad = u3*2,v3*2
u3_pad_,v3_pad_ = 2*N-u3_pad,2*M-v3_pad

u4_pad,v4_pad = u4*2,v4*2
u4_pad_,v4_pad_ = 2*N-u4_pad,2*M-v4_pad

freqs = np.array([[u1,v1],
                  [u1_,v1_],
                  [u2,v2],
                  [u2_,v2_],
                  [u3,v3],
                  [u3_,v3_],
                  [u4,v4],
                  [u4_,v4_],
                  [u1_pad,v1_pad],
                  [u1_pad_,v1_pad_],
                  [u2_pad,v2_pad],
                  [u2_pad_,v2_pad_],
                  [u3_pad,v3_pad],
                  [u3_pad_,v3_pad_],
                  [u4_pad,v4_pad],
                  [u4_pad_,v4_pad_],])

imgs = [img_fft,img_fft_pad]

for i in range(2):
    H = notch_filter(0.1,2,freqs[i*8:8*(i+1)],N*(i+1),M*(i+1))
    img_filt = H*imgs[i]

    plt.figure()

    plt.subplot(2,3,2)
    plt.imshow(img,cmap='gray',aspect='auto')
    plt.title('Det originale bildet')

    plt.subplot(2,3,4)
    plt.imshow(H,cmap='gray',aspect='auto')
    plt.title('Filteret')

    plt.subplot(2,3,5)
    plt.imshow(np.log(np.abs(img_filt)+1),cmap='gray',aspect='auto')
    plt.title('Fourier-spekteret til filtrert bilde')

    plt.subplot(2,3,6)
    plt.imshow(np.abs(ifft2(img_filt)),cmap='gray',aspect='auto')
    plt.title('Filtrert bilde')

img_filt_fft = np.abs(ifft2(img_filt))

# liten juksekode for å vise fram bildet uten nullutvidet område
plt.subplot(2,3,6)

plt.imshow(img_filt_fft[:N,:M],cmap='gray',aspect='auto')
plt.title('Filterert nullutvidet bilde, \nkuttet til original størrelse ')

plt.show()
