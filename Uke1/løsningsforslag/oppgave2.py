D = 10*1e-3    # m
f = 50*1e-3    # m
s = 5          # m
lmb = 500*1e-9 # m

# a)
y = s*1.22*lmb/D
print("deloppgave a: y =",y,'\n')

# b)
y_ = y*f/(s-f)
print("deloppgave b: y' =",y_,'\n')

# c)
T_o = y_
f_o = 1/T_o
print("deloppgave c: T_o = %g, f_o = 1/T_o = %g\n"%(T_o,f_o))

# d)
grense = T_o/2
print("deloppgave d: minste avstand mellom samplingselementer: %g\n"%grense)

# e)
b = 16*1e-3 # m
l = 24*1e-3 # m
print("deloppgave e: antall elementer for å oppfylle samplingsteoremet: %g x %g \n"%(b/grense,l/grense))

# f)
print("deloppgave f: \nb): y' doblet\nc): T_o doblet,f_o halvparten\nd): doblet minste avstand\n")

# g)
print("deloppgave g: bedre fordi minste avstand for å skille to punkter vil bli mindre")
