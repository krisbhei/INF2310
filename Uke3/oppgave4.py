from scipy.misc import imread
import numpy as np
import matplotlib.pyplot as plt
from oppgave2 import hist

def transform_mean_std(img,m_t,sigma_t):
    m_img = np.mean(img)
    sigma_img = np.std(img)

    a = sigma_t/sigma_img
    b = m_t - a*m_img

    T = a*np.arange(255) + b

    return T[img.astype(int)]

if __name__ == '__main__':
    img = imread('mona.png',flatten=True)

    img_t = transform_mean_std(img,m_t=120,sigma_t=10)

    print('- Før transformen:')
    print('middelverdi:',np.mean(img))
    print('standardavvik:',np.std(img))
    print('\n- Etter transformen:')
    print('middelverdi:',np.mean(img_t))
    print('standardavvik:',np.std(img_t))

    plt.figure()
    plt.imshow(img_t,cmap='gray',vmin=0,vmax=255)
    plt.title('transformert bilde')

    plt.figure()
    plt.imshow(img,cmap='gray',vmin=0,vmax=255)
    plt.title('originalbilde')

    hist_img,b = hist(img)
    hist_img_t = hist(img_t.astype(int))[0] # henter ut 0-te element da bins ikke er nødvendig å hente her.

    plt.figure()

    plt.subplot(2,1,1)
    plt.bar(b,hist_img)
    plt.title('histogram til originalbilde')

    plt.subplot(2,1,2)
    plt.bar(b,hist_img_t)
    plt.title('histogram til transformert bilde')

    plt.show()
