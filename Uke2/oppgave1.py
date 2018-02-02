import matplotlib.pyplot as plt
import numpy as np # Her kan man også bruke math-modulen
from scipy.misc import imread

from oppgave3 import forlengs_mapping,baklengs_mapping # for å kunne bruke transformkoeffsientene

th = 33               # grader
th_rad = th*np.pi/180 # radianer - husk at trigonometrise funksjoner antar vinkler i radianer!

## Finne transformkoeffsientene:

# 1 - sett opp rotasjonsmatrisen:
a0 = np.cos(th_rad)
a1 = -np.sin(th_rad)
a2 = 0

b0 = np.sin(th_rad)
b1 = np.cos(th_rad)
b2 = 0

rotasjon_mat = np.array([[a0,a1,a2],[b0,b1,b2],[0,0,1]])

# 2 - sett opp translasjonsmatrisen:
x = 207
y = 421

translasjon_mat_sentrere = np.array([[1,0,x],[0,1,y],[0,0,1]]) # for å sette senter til bildet lik (x,y)
translasjon_mat_tilbake = np.array([[1,0,-x],[0,1,-y],[0,0,1]]) # for å sette senter tilbake til (0,0)

# 3 - multiplisér matrisene for å finne koeffsientene:-
transform = translasjon_mat_sentrere @ rotasjon_mat @ translasjon_mat_tilbake
# Det samme som: transform = np.matmul(translasjon_mat_sentrere,np.matmul(rotasjon_mat,translasjon_mat_tilbake))


## Nå har vi transformkoeffsientene - gir de mening?
## Dette kan man sjekke ved inspeksjon ved å bruke forlengs- eller baklengs-mapping:
img = imread('mona.png',flatten=True)

plt.figure()

img_forlengs = forlengs_mapping(img,transform)
plt.imshow(img_forlengs,cmap='gray',vmin=0,vmax=255)
plt.title("Forlengs mapping")
plt.savefig("mona_rotert_forlengs.svg") # for å lagre bildet i samme mappe.
# Filformatet .svg har bare blitt brukt for å være kompatibel med generingen av html-koden for denne siden. Det går helt fint å bruke andre filformater.


plt.figure()

img_baklengs = baklengs_mapping(img,transform)
plt.imshow(img_baklengs,cmap='gray',vmin=0,vmax=255)
plt.title("Baklengs mapping")
plt.savefig("mona_rotert_baklengs.svg")


plt.figure()

img_baklengs = baklengs_mapping(img,transform,True)
plt.imshow(img_baklengs,cmap='gray',vmin=0,vmax=255)
plt.title("Baklengs mapping med bilineær interpolasjon")
plt.savefig("mona_rotert_baklengs_bilin.svg")

plt.show()
 # ...og bildet ser rotert ut - hurra! For å teste om den faktisk roterer den vinkelen som den skal, er det bare å teste med
 # andre verdier for th som du kan tenke på forhånd hvordan bildet vil se ut.
 # For å sjekke om den faktisk roterer om et gitt punkt, kan man f.eks prøve å rotere om N/2 og M/2.
