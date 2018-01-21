import numpy as np

print("- vektorer -")
# Lage to 1 x 3 matriser:
a = np.array([1,2,3])
b = np.array([11,12,13])

print("a =",a)
print("b =",b)

# elementvis addisjon mellom vektorene
print("a+b =",a+b)

# elementvis multiplikasjon mellom vektorene
print("a*b =",a*b)

# elementvis addisjon mellom en skalar og vektor
print("3 addert med hvert element i a:",3+a)

# elementvis multiplasjon mellom en skalar og vektor
print("3 multiplisert med hvert element i a:",3*a)

print("\n- matriser -")
# Lage to 2 x 2 matriser:
a = np.array([[1,2],[3,4]]) # [1,2] er nå 0-te rad, [3,4] er 1-te rad
b = np.array([[11,12],[13,14]])

print("a =",a)
print("b =",b)

# elementvis addisjon mellom matrisene
print("a+b =",a+b)

# elementvis multiplikasjon mellom matrisene
print("a*b =",a*b)
