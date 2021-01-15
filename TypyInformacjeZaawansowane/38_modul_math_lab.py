'''1. Zaimportuj moduł math

2. Oto wzory pozwalające na wykonanie konwersji stopni na radiany i radianów na stopnie:

1° = (π * rad)/180
1 rad = 180°/π
3. Zadeklaruj zmienną degree i przypisz jej wartość 360. Wylicz i wyświetl ile wynosi wartość radianów dla 360 stopni

4. Zmień wartość zmiennej degree na 45 stopni i powtórz obliczenia

5. ... ale moduł math ma funkcję radians, która wykonuje konwersję stopni na radiany! Porównaj wyniki zwracane przez Twoje obliczenia z obliczeniami funkcji radians.

6. Pizzeria oferuje pizze:

small - promień 22 cm, cena, 11.50

big - promień 27 cm, cena 15.60

family - promień 38cm, cena 22.00

Zadeklaruj zmienne small_pizza_r, big_pizza_r, family_pizza_r oraz small_pizza_price, big_pizza_price, family_pizza_price i zapisz w nich w/w wartości.

7. Oblicz pole powierzchni pizz w metrach kwadratowych

8. Wyznacz cenę metra kwadratowego pizzy small, big i family

9. Zobacz jakie inne funkcje są dostępne w module math. Możesz w tym celu odwiedzić stronę

https://docs.python.org/2/library/math.html

lub wykonać polecenie:

math_ls = dir(math)
print(math_ls)'''

import math
degree = 360
radian = degree * math.pi /180
print("%d stopni to %f radianów" % (degree, radian))
print(math.radians(degree))
print('-----------------------------------------------\n')

degree = 45
radian = degree * math.pi /180
print("%d stopni to %f radianów" % (degree, radian))
print(math.radians(degree))
print('-----------------------------------------------\n')

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00
#pi*r**2
small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2

print('small:', small_pizza_r, small_pizza_price, small_area)
print('big:', big_pizza_r, big_pizza_price, big_area)
print('family:', family_pizza_r, family_pizza_price, family_area)
print('-----------------------------------------------')
print('small:', small_pizza_price / small_area)
print('big:', big_pizza_price / big_area)
print('family:', family_pizza_price / family_area)
print('-----------------------------------------------\n')

#listowanie zawartości/komend modułu
math_ls = dir(math)
print(math_ls)

