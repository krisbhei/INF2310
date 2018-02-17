from oppgave6 import *

# Definere en Gauss-histogram som eksempel.
# Mulig å også bruke:
# gauss = lambda x,mu,std: np.exp(-0.5*((x-mu)/std)**2)/np.sqrt(2*np.pi*std**2)
def gauss(x,mu,std):
    return np.exp(-0.5*((x-mu)/std)**2)/np.sqrt(2*np.pi*std**2)


G = 256
intensiteter = np.linspace(0,G-1,G)

img = imread('mona.png',flatten=True)

# Spesifisér ønsket middelverdi og standardavvik til Gauss-en:
mu = float(input('Middelverdi = '))
std_ = float(input('Standardavvik = '))
q = gauss(intensiteter,mu,std_)
q /= np.sum(q) # For aa soerge for at histogrammet er normalisert

img_T = histogramtilpasning(img,q)

# For å sjekke om transformen gir et bilde med samme statistiske egenskaper
# som den spesifiserte Gaussen:
print('\nSum av ønsket histogram: ',np.sum(q))
print('Middelverdi til transformert bilde: ',np.mean(img_T.flatten()))
print('Standardavvik til transformert bilde: ',np.std(img_T.flatten()))

plot_histogramtilpasning(img,img_T,q)
