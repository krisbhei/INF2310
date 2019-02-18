from oppgave6 import *
import numpy as np
from imageio import imread

# Definerer et uniformt histogram over G intensiteter.
# Mulig å også bruke:
# gauss = lambda G: np.ones(G)/G
def uniform(G):
    return np.ones(G)/G

G = 256
intensiteter = np.arange(G)

img = imread('mona.png',as_gray=True)

q = uniform(G)

img_T = histogramtilpasning(img,q)

plot_histogramtilpasning(img,img_T,q)
