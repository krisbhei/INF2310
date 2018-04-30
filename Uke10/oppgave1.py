import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from histogram_image import *

img_clean = imread('textImage_clean.png',flatten=True)
N,M = img_clean.shape

light_factor = 50
light_mask = np.tile((np.linspace(1,M,M)-M/2)/M,(N,1))
img_light = img_clean + light_factor*light_mask

# a
h_img,ax = hist(img_clean)

plt.figure()

plt.subplot(2,1,1)
plt.bar(ax,h_img)
plt.title('Normalisert histogram')

plt.subplot(2,1,2)
plt.imshow(img_clean,cmap='gray',aspect='auto')
plt.title('img_clean.png')

# b
plt.figure()

plt.subplot(2,3,2)
plt.bar(ax,h_img)
plt.title('Det originale bildets normaliserte histogram')

for c,noise_std in enumerate([10,30,90]):
    img_noisy = img_clean + noise_std*np.random.randn(N,M)
    h = hist(np.round(img_noisy))[0]

    plt.subplot(2,3,c+4)
    plt.bar(ax,h)
    plt.title('Det normaliserte histogrammet\ntil bildet med noise_std = %d'%noise_std)

# c og d
plt.figure()

plt.subplot(2,3,2)
plt.bar(ax,h_img)
plt.title('Det originale bildets normaliserte histogram')

for c,light_factor in enumerate([50,75,100]):
    img_light = img_clean + light_factor*light_mask
    h = hist(np.round(img_light))[0]

    plt.subplot(2,3,c+4)
    plt.bar(ax,h)
    plt.title('Det normaliserte histogrammet\ntil bildet med light_factor = %d'%light_factor)


# e

# ser på det gitte eksemepelet  fra oppgaven
noise_std = 30
img_noisy = img_clean + noise_std*np.random.randn(N,M)
background_pixels = img_noisy[img_clean < 150]
foreground_pixels = img_noisy[img_clean > 150]

B = background_pixels.size/(N*M)
F = foreground_pixels.size/(N*M)

h_background = hist(np.round(background_pixels))[0]
h_foreground = hist(np.round(foreground_pixels))[0]

hist_background = B*h_background
hist_foreground = F*h_foreground

plt.figure()

plt.plot(ax,hist_background)
plt.plot(ax,hist_foreground)

plt.title('Normaliserte histogram')

# f
# Fant skjæringspunkt ved intensitet omtrent lik 168
T = 168

error_foreground = np.sum(hist_background[T:])*N*M
error_background = np.sum(hist_foreground[:T])*N*M

print("Antall feilklassifiserte forgrunnspiksler: %g"%error_foreground)
print("Antall feilklassifiserte bakgrunnspiksler: %g"%error_background)

# g
h_noisy = hist(np.round(img_noisy))[0]

plt.figure()

plt.plot(ax,hist_foreground)
plt.plot(ax,hist_background)
plt.plot(ax,hist_background+hist_foreground)
plt.plot(ax,h_noisy)

plt.title('Normaliserte histogram')
plt.legend(['foreground','background','foreground+background','image'])

plt.show()
