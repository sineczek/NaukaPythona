import random

mojeNumerki = []

while len(mojeNumerki) <= 7:

    nowyNumerek = random.randint(1,49) #randint generuje włacznie z granicznymi
    if nowyNumerek in mojeNumerki:
        print('To już było ...', nowyNumerek)
        continue
    mojeNumerki.append(nowyNumerek)

print('Liczymy, że wypadną numerki w najbliższym losowaniu:', mojeNumerki)
