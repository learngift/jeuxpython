a = []
i = 0
while i <= 20:
    a.append(i ** 2)
    i = i + 1

b = []
for i in range(21):
    b.append(i ** 2)

c = [ i ** 2 for i in range(21) ]

from math import * # pour avoir la constante pi et la fonction sqrt

L = [2, 5, 1, pi/2, sqrt(2)]

# print('Le plus petit élément est : ' + str(min(L)) +
#         ', le plus grand est : ' + str(max(L)))
print(f'Le plus petit élément est :{min(L)}, le plus grand est {max(L)}')

L1 = sorted(L)

L2 = sorted(L, reverse=True)

L.insert(1, 'un')

L = L[:3] + [8, 10] + L[3:]

L1 = [0.1, -3, 4.2, 15, -7, 4.2, -17]

NL = []
for e in L1:
    if e >= 0:
        NL.append(e)
L1 = NL

# la meilleure façon
L1 = [ e for e in L1 if e >= 0 ]

L2 = [ 'un', 251.2, "arbre", 250, 98, "c'est", 56, "beau", 5689]
for e in L2:
    if type(e) == str:
        print(e)

for i, e in enumerate(L1):
    print(f'{i} -> {e}')

# indice du max et du min
i_max = 0
i_min = 0
v_max = L1[0]
v_min = v_max
for i, e in enumerate(L1):
    if e > v_max:
        v_max = e
        i_max = i
    elif e < v_min:
        v_min = e
        i_min = i
print(f'min {i_min} -> {v_min}, max {i_max} -> {v_max}')

def f(x):
    return sqrt(16 - ((x-1) ** 2))

Lx = [ -2.8, -2.4, -2, -1, 0, 1, 2, 3, 4, 4.4, 4.8 ]

image1 = [ f(x) for x in Lx ]
image2 = []
for x in Lx:
    image2.append(f(x))

i_max = 0
v_max = L1[0]
for i, e in enumerate(image1):
    if e > v_max:
        v_max = e
        i_max = i
print(f'max {i_max} -> {v_max}')
