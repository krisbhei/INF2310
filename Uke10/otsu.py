import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from histogram_image import *
from skimage import filters

def otsu(img):
    p = hist(img)[0]

    G = len(p)

    P1 = np.zeros(G) # Kumulativt sannsynlighet for klasse 1
    for i in range(G):
        for k in range(i+1): # i+1 for at siste verdi til k skal bli lik i
             P1[i] += p[k]

    mu_k = np.zeros(G) # Kumulativ middelverdi
    for i in range(G):
        for k in range(i+1):
            mu_k[i] += k*p[k]

    mu = 0 # Global middelverdi
    for i in range(G):
        mu += i*p[i]

    # Gå gjennom hver mulige terksel, og finn maksimum.
    # Koden regner ut varians for hver mulige terksel i og sjekker om
    # det er den største. Hvis så, vil tilhørende terksel, i,
    # 'lagres' i variabelen T.
    T = 0
    stoerste_varians_B = 0
    for i in range(G):
        if (P1[i] != 0 and P1[i] != 1): # Unngå å dele på null
            varians_B = (mu_k[i] - mu*P1[i])**2/(P1[i]*(1-P1[i]))
            if varians_B > stoerste_varians_B:
                stoerste_varians_B = varians_B
                T = i

    return T

if __name__ == '__main__':
    img_clean = imread('textImage_clean.png',flatten=True)
    N,M = img_clean.shape

    noise_std = 50
    img_noisy = img_clean + noise_std*np.random.randn(N,M)
    img_noisy_255 = np.round(from0to255(img_noisy))

    T = otsu(img_noisy_255)
    T_skimage = filters.threshold_otsu(img_noisy_255)

    print(T,T_skimage)
