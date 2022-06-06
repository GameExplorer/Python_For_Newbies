from random import *

seed(8)

metov = 0
pozicija = 0
na_5 = 0

while na_5 < 100:
    met = randint(1, 6)
    pozicija = (pozicija + met) % 6
    if pozicija == 5:
        na_5 += 1
    metov += 1

print(metov)