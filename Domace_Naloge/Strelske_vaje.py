from math import *

g = 10
kot = float(input("Vnesi kot (v stopinjah)"))
v = float(input("Vnesi hitrost (v m/s)"))
kot_rad = radians(kot)
razdalja = v ** 2 * sin(2 * kot_rad) / g
print("Kroglo bo odneslo", razdalja, "metrov daleč")