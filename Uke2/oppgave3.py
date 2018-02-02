import numpy as np

def forlengs_mapping(img,transform):
    # Henter ut koeffsientene fra transformasjonsmatrisen
    a = transform[0,:]
    b = transform[1,:]

    a0,a1,a2 = a
    b0,b1,b2 = b

    N,M = img.shape
    resultat = np.zeros((N,M))

    for x in range(N):
        for y in range(M):
            x_ = int(np.round(a0*x + a1*y + a2))
            y_ = int(np.round(b0*x + b1*y + b2))
            if 0 <= x_ <= N-1 and 0 <= y_ <= M-1:
                resultat[x_,y_] = img[x,y]

    return resultat

def baklengs_mapping(img,transform,bilinear=False):
    # antar transformmatrisen er på formen som i slide 6.
    # Dette betyr at matrisen med koeffsientene må inverteres
    transform_inv = np.linalg.inv(transform)

    a = transform_inv[0,:]
    b = transform_inv[1,:]

    a0,a1,a2 = a
    b0,b1,b2 = b

    N,M = img.shape
    resultat = np.zeros((N,M))

    for x_ in range(N):

        for y_ in range(M):

            x = a0*x_ + a1*y_ + a2
            y = b0*x_ + b1*y_ + b2

            if 0 <= x <= N-1 and 0 <= y <= M-1: # for å sjekke om koordinatene kan i det hele tatt brukes

                if bilinear: # bilineær interpolasjon - se slide 19

                    x0 = int(np.floor(x)); x1 = int(np.ceil(x))
                    y0 = int(np.floor(y)); y1 = int(np.ceil(y))
                    dx = x - x0
                    dy = y - y0

                    p = img[x0,y0] + (img[x1,y1] - img[x0,y0])*dx
                    q = img[x0,y1] + (img[x1,y1] - img[x0,y1])*dx

                    value = p + (q-p)*dy

                else:

                    x = int(np.round(x))
                    y = int(np.round(y))
                    value = img[x,y]

                resultat[x_,y_] = value

    return resultat
