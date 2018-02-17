from oppgave6 import *
import numpy as np
from scipy.misc import imread

# Definerer et uniformt histogram over G intensiteter.
# Mulig å også bruke:
# gauss = lambda G: np.ones(G)/G
def uniform(G):
    return np.ones(G)/G

G = 256
intensiteter = np.linspace(0,G-1,G)

img = imread('mona.png',flatten=True)

q = uniform(G)

img_T = histogramtilpasning(img,q)

plot_histogramtilpasning(img,img_T,q)
