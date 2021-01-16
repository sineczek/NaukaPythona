'''1. Zaimportuj moduł random

2. Wylosuj 10 liczb z zakresu 1-100

3. To nieco dłuższe zadanie:

do zmiennej number1 wylosuj liczbę całkowitą z zakresu 1-100

twoim celem będzie losowanie liczb losowych tak długo, aż znowu wylosujesz liczbę number1. Dodatkowo chcemy policzyć ile prób jest do tego potrzebnych

do zmiennej counter zapisz 1

do zmiennej number2 wylosuj liczbę z zakresu 1-100

wyświetl numer próby (counter) i wylosowaną liczbę (number2)

Tak długo jak długo number1 jest inne niż number2

zwiększ counter o 1

wylosuj ponownie liczbę number2 (liczba całkowita od 1 do 100)

wyświetl numer próby (counter) i wylosowaną liczbę (number2)

Na zakończenie wyświetl podsumowanie z infromacją o ilości prób

4. Tym razem zbudujesz program losujący skład do rozgrywek "2018 FIFA WORLD CUP RUSSIA". Utwórz zmienną countries jak poniżej:

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
następnie:

losowo wymieszaj kolejność drużyn

utwórz zmienną groupNumber i przypisz jej wartość 0

wykonaj czynność tyle razy ile jest państw na liście countries:

jeżli numer państwa jest podzielny przez 4 (reszta z dzielenia modulo 4 jest równa 0) to:

zwiększ numer grupy o 1

wyświetl napis "----Grupa X----"

każdorazowo wyświetlaj wylosowany kraj

Jak sądzisz, czy w Twojej konfiguracji grup Polska miałaby większe szanse?'''



import random
for int in range(10):
    print(random.randrange(1,100))

number1 = random.randrange(1,100)
number2 = 0
counter = 1

while number2 != number1:
    if number2 != number1:
        number2 = random.randrange(1,100)

        print('próba nr:',counter,'number1:', number1,'number2:',number2)
        counter+=1
    else:
        print('Liczby są równe, number1:',number1,'number2:',number2,'potrzebnych było:',counter,'prób')

#FiFa 2018
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
]
random.shuffle(countries)
groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])






