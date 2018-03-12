import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread

img_rgb = imread('rose_rgb.png',mode='RGB')
img_rgb = img_rgb / np.max(img_rgb)

N,M,tmp = img_rgb.shape
img_ihs = np.zeros((N,M,3))


for x in range(N):
    for y in range(M):
        # Normalisere slik at transformasjonene i
        # slide 27 fra forelesningen om farge

        R = img_rgb[x,y,0]
        G = img_rgb[x,y,1]
        B = img_rgb[x,y,2]

        thr = 1e-7

        if abs(R - G) < thr and abs(G- B) < thr:
            H = 361 # Setter en usannsynlig verdi for å vise at H er udefinert
        else:
            th = np.arccos( 0.5*( (R-G) + (R-B) )/np.sqrt( (R-G)**2 + (R-B)*(G-B) ) )
            th = th*180/np.pi

            H = th if B <= G else 360 - th

        if R + G + B < thr:
            S = 0
            I = 0
        else:
            S = 1 - 3*np.min([R,G,B])/(R+G+B)
            I = (R+G+B)/3

        img_ihs[x,y,0] = I
        img_ihs[x,y,1] = H
        img_ihs[x,y,2] = S

# Slutt - Transform fra RGB til IHS

# Vis fram IHS:
plt.figure()

plt.subplot(2,3,1)
plt.imshow(img_ihs[:,:,0],cmap='gray',aspect='auto')
plt.title('Intensitet I')

plt.subplot(2,3,2)
plt.imshow(img_ihs[:,:,1],cmap='gray',aspect='auto')
plt.title('Hue H')

plt.subplot(2,3,3)
plt.imshow(img_ihs[:,:,2],cmap='gray',aspect='auto')
plt.title('Metning S')

plt.subplot(2,3,5)
plt.imshow(img_rgb,aspect='auto')
plt.title('Original RGB-bilde')

# Lagre intensitet-komponenten fra IHS:
plt.figure()
plt.imshow(img_ihs[:,:,0],cmap='gray')
plt.axis('off')
plt.savefig('rose_gray.png',bbox_inches='tight')

# Finn histogram for hver R,G og B komponent og intensitet og vis frem:

# Lignende funksjon fra Uke3 - oppgave 2:
def hist(img,bins):
    p = np.array([np.sum(img == i) for i in bins])/img.size
    return p

bins = np.arange(255)

R_hist = hist(np.round(img_rgb[:,:,0]*255),bins) # Ganger med 255 for å tilpasse til egendefinert
                                                 # hist-funksjonen.
G_hist = hist(np.round(255*img_rgb[:,:,1]),bins)
B_hist = hist(np.round(255*img_rgb[:,:,2]),bins)

I_hist = hist(np.round(img_ihs[:,:,0]*255),bins)

# Vis frem histogram:
plt.figure()

plt.subplot(1,3,1)
plt.bar(bins,R_hist,color=[1,0,0],alpha=0.3)
plt.bar(bins,G_hist,color=[0,1,0],alpha=0.3)
plt.bar(bins,B_hist,color=[0,0,1],alpha=0.3)
plt.title('Histogram av R,G og B komponent')
plt.legend(['R','G','B'])

plt.subplot(1,3,2)
plt.bar(bins,I_hist,color=[0,0,0])
plt.title('Histogram av I - komponent')

plt.subplot(1,3,3)
plt.bar(bins,I_hist,color=[0,0,0],alpha=0.5)
plt.bar(bins,R_hist,color=[1,0,0],alpha=0.3)
plt.bar(bins,G_hist,color=[0,1,0],alpha=0.3)
plt.bar(bins,B_hist,color=[0,0,1],alpha=0.3)
plt.title('Histogram av I,R,G og B komponent')
plt.legend(['I','R','G','B'])

# Gir IHS transformen mening?
# Mulig å ta invers for å sjekke. (gitt at invers blir riktig implementert ... )

img_ihs_inv =  np.zeros((N,M,3))

grad2rad = lambda th: th*np.pi/180 # Funksjon som konverterer fra grader til radiner

# Fra IHS til RGB:

for x in range(N):
    for y in range(M):
        I = img_ihs[x,y,0]
        H = img_ihs[x,y,1]
        S = img_ihs[x,y,2]

        if H == 361:
            R = I
            G = I
            B = I
        elif H <= 120:
            R = I*(1 + S*np.cos(grad2rad(H))/np.cos(grad2rad(60 - H)))
            B = I*(1-S)
            G = 3*I - (R+B)
        elif H <= 240 :
            H -= 120
            R = I*(1-S)
            G = I*(1 + S*np.cos(grad2rad(H))/np.cos(grad2rad(60 - H)))
            B = 3*I - (R+G)
        else:
            H -= 240
            G = I*(1-S)
            B = I*(1 + S*np.cos(grad2rad(H))/np.cos(grad2rad(60 - H)))
            R = 3*I - (G+B)

        img_ihs_inv[x,y,:] = [R,G,B]

# Slutt - Fra IHS til RGB

# Har transformen fra IHS til RGB gitt mer eller mindre originalbilde tilbake?

err = np.abs(img_rgb - img_ihs_inv) # Må sammenligne med normalisert RGB
                                            # siden formlene i sliden antar normaliserte
                                            # RGB-verdier.
print("Største feil fra RGB til IHS tilbake til RGB:",np.max(err))

plt.figure()

plt.subplot(1,3,1)
plt.imshow(img_ihs_inv,aspect='auto')
plt.title('Fra RGB til IHS og tilbake til RGB')

plt.subplot(1,3,2)
plt.imshow(img_rgb,aspect='auto')
plt.title('Opprinnelig RGB bilde')

plt.subplot(1,3,3)
plt.imshow(err,aspect='auto')
plt.title('Differanse mellom bildene')

plt.show()


#
# plt.show()
