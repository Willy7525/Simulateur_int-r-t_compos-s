import numpy as np


vi =float(input("Valeur initial\n"))
vstock = vi
dca = float(input("DCA mensuel\n"))
intérêt = float(input("intérêt annuel\n"))/(12*100)
n = float(input("nombre d'années\n")) * 12

for i in range(int(n)):
    vi = vi + dca
    vi = vi * (1 + intérêt)

print("Valeur finale : ", int(vi))
print("Valeur versements : ", int(dca*n + vstock))
print("valeur intérêts : ", int(vi-(dca*n)-vstock) )

