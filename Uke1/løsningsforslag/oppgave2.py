D = 10*1e-3    # m
f = 50*1e-3    # m
s = 5          # m
lmb = 500*1e-9 # m

# a)
y = s*1.22*lmb/D
print("y =",y)

# b)
y_ = y*f/(s-f)
print("y' =",y_)

# c)
T_o = y_
f_o = 1/T_o
print("T_o = %g, f_o = 1/T_o = %g"%(T_o,f_o))

# d)
grense = T_o/2
print("minste avstand mellom samplingselementer: %g"%grense)

# e)
b = 16*1e-3 # m
l = 24*1e-3 # m
print("antall elementer for å oppfylle samplingsteoremet: %g x %g"%(b/grense,l/grense))

# f)
print("b): y' doblet\nc): T_o doblet,f_o halvparten\nd): doblet minste avstand")

# g)
print("bedre fordi minste avstand for å skille to punkter vil bli mindre")
