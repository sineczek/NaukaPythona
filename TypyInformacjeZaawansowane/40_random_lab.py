'''1. Rzuć kostką. Co? Nie masz kostki do gry pod ręką? W takim razie:



Zaimportuj moduł random

Zainicjiuj zmienne min =1 i max = 6

Do zmiennej dice zapisz wynik losowania liczby między min, a max. W ten sposób zasymulowaliśmy rzut kostką.

Napisz sekwencję poleceń if/elif/else, która w zależności od wylosowanej wartości wyświetli:



1:

 o


2:
  o

o

3:
  o
 o
o

4:
o o

o o

5:
o o
 o
o o

6:
o o
o o
o o


2. Trochę zmieniamy temat. Rzuć pięcioma kostkami:



zadeklaruj zmienną dices jako pustą listę

pięć razy wylosuj liczbę z zakresu min do max i wynik dopisz do listy dices

posortuj listę dices

wyświetl zawartość zmienej dices '''

d1 = '''

o

'''
d2='''
  o

o
'''
d3='''
  o
 o
o
'''
d4='''
o o

o o
'''
d5='''
o o
 o
o o
'''
d6='''
o o
o o
o o
'''
min =1
max = 6
import random


dice=random.randrange(min,max)
print(dice)
if dice == 1:
    print(d1)
elif dice == 2:
    print(d2)
elif dice == 3:
    print(d3)
elif dice == 4:
    print(d4)
elif dice == 5:
    print(d5)
else:
    print(d6)

print('----------------------------------------------\n')

dices =[]
d1 = '''

o

'''
d2='''
  o

o
'''
d3='''
  o
 o
o
'''
d4='''
o o

o o
'''
d5='''
o o
 o
o o
'''
d6='''
o o
o o
o o
'''
min =1
max = 6
import random

for i in range(5):
    dice=random.randrange(min,max)
    print(dice)
    dices.append(dice)
    if dice == 1:
        print(d1)
    elif dice == 2:
        print(d2)
    elif dice == 3:
        print(d3)
    elif dice == 4:
        print(d4)
    elif dice == 5:
        print(d5)
    else:
        print(d6)
print(dices)