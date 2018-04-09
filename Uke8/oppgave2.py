import matplotlib.pyplot as plt
from basisbilder import *

M = 256; N = 512

# a
u = 10; v = 10

sin_img = lag_basis(u,v,M,N)

plt.figure()
plt.imshow(sin_img,cmap='gray')
plt.title('Sinus med frekvens (u,v) = (%d,%d)'%(u,v))

# b
cos_img = lag_basis(u,v,M,N,False)

print("sum(cos*sin) = %g\n"%np.sum(sin_img*cos_img))

# c
u2,v2 = 86,45

sin2_img = lag_basis(u2,v2,M,N)
cos2_img = lag_basis(u2,v2,M,N,False)

print("sum(cos2*sin2) = %g"%np.sum(sin2_img*cos2_img))
print("sum(cos*sin2) = %g"%np.sum(sin2_img*cos_img))
print("sum(cos*sin2) = %g"%np.sum(sin2_img*cos_img))
print("sum(cos2*sin) = %g"%np.sum(sin_img*cos2_img))
print("sum(cos2*sin) = %g\n"%np.sum(sin_img*cos2_img))

# d
u3,v3 = 246,502

sin3_img = lag_basis(u3,v3,M,N)
cos3_img = lag_basis(u3,v3,M,N,False)

plt.figure()

plt.subplot(2,2,1)
plt.imshow(cos_img,cmap='gray',aspect='auto')
plt.title('Cosinus med frekvens (u,v) = (%d,%d)'%(u,v))

plt.subplot(2,2,2)
plt.imshow(sin_img,cmap='gray',aspect='auto')
plt.title('Sinus med frekvens (u,v) = (%d,%d)'%(u,v))

plt.subplot(2,2,3)
plt.imshow(cos3_img,cmap='gray',aspect='auto')
plt.title('Cosinus med frekvens (u,v) = (%d,%d)'%(u3,v3))

plt.subplot(2,2,4)
plt.imshow(sin3_img,cmap='gray',aspect='auto')
plt.title('Sinus med frekvens (u,v) = (%d,%d)'%(u3,v3))

if np.all(np.abs(sin3_img - (-sin_img)) < 1e-10):
    print("sinus med frekvens (%d,%d) = - sinus med frekvens (%d,%d)"%(u,v,u3,v3))
if np.all(np.abs(cos3_img - cos_img) < 1e-10):
    print("cosinus med frekvens (%d,%d) = cosinus med frekvens (%d,%d)\n"%(u,v,u3,v3))

# e
print("sum(sin*sin) = %g"%np.sum(sin_img*sin_img))
print("sum(cos*cos) = %g"%np.sum(cos_img*cos_img))

#plt.show()
