from imageio import imread
import numpy as np
import matplotlib.pyplot as plt

def hist1(img):
    # Anta at bildet img har verdier mellom 0 og 255
    G = 256

    intensities = np.arange(G)
    p = np.array([np.sum(img == i) for i in intensities])/img.size
    return p, intensities

def hist2(img):
    # Denne funksjonen gjør det samme som hist1.
    # Forskjellen er at denne funksjonen gjør ikke vektorisering, og er ment for å vise
    # mer detaljert hva som faktisk skjer i hist1-metoden for å regne ut p.
    G = 256

    intensities = np.arange(G)

    p = np.zeros(G)
    for i in range(G):
        p[i] = np.sum(img == intensities[i])

    p /= img.size

    return p, intensities

if __name__ == '__main__':

    img = imread('mona.png',as_gray=True)

    p1, bins1 = hist1(img)
    p2, bins2 = hist2(img)
    p_np, bins_np = np.histogram(img, bins = 256, range = (0, 256), density = True) # for å sammenligne med numpy

    # Visualiser histogrammene
    plt.subplot(1,3,1)
    plt.title('hist1')
    plt.bar(bins1, p1)

    plt.subplot(1,3,2)
    plt.title('hist2')
    plt.bar(bins2, p2)

    plt.subplot(1,3,3)
    plt.title('np.histogram')
    plt.bar(bins_np[:-1], p_np)

    plt.show()

    # En måte å teste om funksjonene gjør det samme som fra numpy:
    thr = 1e-8
    print('Gjør hist1 det samme som np.histgram?:', np.all(np.abs(p1 - p_np) < thr))
    print('Gjør hist2 det samme som np.histogram?:', np.all(np.abs(p2 - p_np) < thr))
    print('Gjør hist1 det samme som hist2?:', np.all(np.abs(p2 - p1) < thr))
