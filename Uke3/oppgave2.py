from scipy.misc import imread
import numpy as np
import matplotlib.pyplot as plt

# Anta at img har verdier mellom 0 og 255
def hist(img):
    bins = np.arange(255)
    p = np.array([np.sum(img == i) for i in bins])/img.size
    return p,bins

if __name__ == '__main__':

    img = imread('mona.png',flatten=True)
    p,bins = hist(img)

    plt.bar(bins,p)
    plt.show()
