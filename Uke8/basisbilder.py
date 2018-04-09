import numpy as np

def lag_basis(u,v,M,N,sinus=True):
    y = np.tile(np.arange(0,N),(M,1)) # np.tile tilsvarer matlabs repmat
    x = np.tile(np.reshape(np.arange(0,M),(M,1)),(1,N))

    if sinus:
        return np.sin(-2*np.pi*(u/M*x + v/N*y))

    return np.cos(2*np.pi*(u/M*x + v/N*y))
