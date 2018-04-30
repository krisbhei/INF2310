import numpy as np

# Fra løsningsforslag til uke3 - oppgave 2
def hist(img):
    bins = np.arange(256)
    p = np.array([np.sum(img == i) for i in bins])/img.size
    return p,bins

def from0to255(img):
    return ((img- np.min(img))*255)/(np.max(img) - np.min(img))
