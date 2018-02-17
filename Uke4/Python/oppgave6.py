
from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np

"""
histogramtilpasning(img,q)
Histogramtilpasser et 8-bits innbilde img til histogram q

Argumenter:
    * img: innbildet
    * q: histogram innbildet (ideelt) skal få
Returnerer:
    * Innbildet med histogram tilnærmet lik q
"""
def histogramtilpasning(img,q):
    # Antar 8-bit
    G = 256;

    # Finn innbildets histogram og deretter dets kumulative histogram:
    c = finn_histogram_bilde(img)[1]

    # Finn det kumulative histogrammet til q:
    cq = np.cumsum(q)

    # Transformér innbildet img:
    T = np.zeros(G)

    for i in range(G):
        T[i] = np.argmin(np.abs(c[i] - cq))

    return T[img.astype(int)] # T anvendes på hvert element i bildet img


"""
plot_histogramtilpasning(img,img_T,q)
Plotter innbildet img og det histogramtilpassede bildet img_T med bildenes histogram
og kumulative histogram.

Argumenter:
    * img: Innbildet
    * img_T: Det histogramtilpassede bildet
    * q: Histogrammet som img er tilpasset til.
Returnerer:
    Ingenting. Skal vise frem ett vindu.
"""
def plot_histogramtilpasning(img,img_T,q,save=False):
    G = 256
    intensiteter = np.linspace(0,G-1,G)

    # Finn histogrammene til innbildet:
    p,c = finn_histogram_bilde(img)

    # Finn histogrammene til det histogramtilpassede bildet:
    p_T,c_T = finn_histogram_bilde(img_T)

    # Finn det kumulative histogramet til q for plottingen sin del:
    c_q = np.cumsum(q)

    plt.figure()

    plt.subplot(3,2,1)
    plt.imshow(img_T,cmap='gray')
    plt.title('Transformert bilde')
    plt.axis('off')

    plt.subplot(3,2,2)
    plt.imshow(img,cmap='gray')
    plt.title('Original bilde')
    plt.axis('off')

    plt.subplot(3,2,3)
    plt.bar(intensiteter,p_T,edgecolor='none')
    plt.title('Histogram til det transformerte bildet')
    plt.plot(intensiteter,q,'r',linewidth=2)
    plt.legend(['ønsket','bildets'])

    plt.subplot(3,2,4)
    plt.bar(intensiteter,p,edgecolor='none')
    plt.title('Histogram til det originale bildet')

    plt.subplot(3,2,5)
    plt.bar(intensiteter,c_T,edgecolor='none')
    plt.title('Kumulativ histogram til det transformerte bildet')
    plt.plot(intensiteter,c_q,'r')
    plt.legend(['ønsket','bildets'])

    plt.subplot(3,2,6)
    plt.bar(intensiteter,c,edgecolor='none')
    plt.title('Kumulativ histogram til det originale bildet')

    plt.show()


"""
finn_histogram_bilde(img)
Finner det det normaliserte og kumulative histogrammet til bildet img

Argumenter:
    * img: Bildet som funksjonen skal finne histogrammene til.
Returnerer:
    * p: Det normaliserte histogrammet.
    * c: Det kumulative histogrammet.
"""
def finn_histogram_bilde(img):
    p = np.array([np.sum(img.astype(int) == i) for i in range(256)])/img.size
    c = np.cumsum(p)
    return p,c
