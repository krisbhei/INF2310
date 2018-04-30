import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from histogram_image import *
from skimage import filters

def riddler_calvard(img,mu_background,mu_foreground):
    Tprev = 0
    T = (mu_background+mu_foreground)/2

    while abs(Tprev - T) > 1e-14:
        mu_background = (img[img <= T]).mean()
        mu_foreground = (img[img > T]).mean()

        Tprev = T
        T = (mu_background+mu_foreground)/2

    return T

def otsu(img):
    p = hist(img)[0]

    G = len(p)

    c = np.array([np.sum(p[:k]) for k in range(1,G+1)])

    mu_c = np.array([np.sum((np.arange(k))*p[:k]) for k in range(1,G+1)])
    mu = np.sum(np.arange(G)*p)

    var_B = (mu_c[:G-1] - mu*c[:G-1] )**2/(c[:G-1] *(1-c[:G-1] ))

    k = np.where(var_B == np.max(var_B))

    return k


if __name__ == '__main__':
    img_clean = imread('textImage_clean.png',flatten=True)
    N,M = img_clean.shape

    noise_std = 50
    img_noisy = img_clean + noise_std*np.random.randn(N,M)
    img_noisy_255 = from0to255(img_noisy)

    T = riddler_calvard(img_noisy,125,150)
    print("R&C: %g"%T)

    img_thr = np.zeros((N,M))
    img_thr[img_noisy > T] = 1

    plt.figure()

    plt.subplot(1,2,1)
    plt.imshow(img_thr,cmap='gray',aspect='auto')
    plt.title('Tersklet bilde ved R&C')

    plt.subplot(1,2,2)
    plt.imshow(img_noisy,cmap='gray',aspect='auto')
    plt.title('Det originale bildet')

    T = otsu(np.round(img_noisy_255))

    img_thr = np.zeros((N,M))
    img_thr[img_noisy_255 > T] = 1

    plt.figure()

    plt.subplot(1,3,1)
    plt.imshow(img_thr,cmap='gray',aspect='auto')
    plt.title('Tersklet bilde ved Otsu')

    plt.subplot(1,3,2)
    plt.imshow(img_noisy,cmap='gray',aspect='auto')
    plt.title('Det originale bildet')

    T1 = filters.threshold_otsu(img_noisy_255)
    img_thr = np.zeros((N,M))
    img_thr[img_noisy_255 > T1] = 1

    plt.subplot(1,3,3)
    plt.imshow(img_thr,cmap='gray',aspect='auto')
    plt.title('Tersklet bilde ved Otsu - skipy')

    print("otsu: %g"%T)
    print("otsu-scipy: %g"%T1)
    plt.show()
