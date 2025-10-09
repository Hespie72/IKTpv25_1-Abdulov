from math import *
import math #iport oli valasti tehtud
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #float ei olnud
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*math.sqrt(2) #sqrt ei olnud 
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #float ei olnud
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #float ei olnud
S=b*c
print('Ristküliku pindala', round(S, 2))
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P, 2))
di=math.sqrt(b**2+c**2)
print("Ristküliku diagonaal", round(di, 2))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #float ei olnud ja " ei olnud 
d=2*r
print("Ringi läbimõõt", round(d, 2)) #, ei olnud
S=pi*r**2
print("Ringi pindala", round(S, 2))
C=2*pi*r #* ei olnud
print("Ringjoone pikkus", round(C, 2)) #teine ) ei olnud