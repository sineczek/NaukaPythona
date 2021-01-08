'''Dzięki znajomości Pythona dostajesz pracę w BTAW (Bardzo Tajna Agencja Wywiadowcza).
Od poprawnego rozwiązania poniższych zadań zależy złamanie algorytmów szyfrujących wroga:

1. Dana jest zakodowana informacja w postaci tabeli:
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej. W tym celu:

trzeba wykonać analizę po dwa elementy na raz

zmienna sterująca i przyjmie wartość od zera do ..... ?

przy pomocy pętli while i sterującej nią zmiennej i analizuj po dwie wartości z listy na raz

wyświetl analizowane wartości

jeżeli pierwsza z nich do kwadratu jest równa drugiej, to wyświetl napis "FOUND"

2. Pracujemy z tą samą listą co poprzednio. Tym razem należy analizować po 3 wartości na raz.
Interesuje nas odnalezienie takich 3 liczb, że pierwsza do kwadratu równa się drugiej, a druga do kwadratu równa się trzeciej.
Właściwie do tego zadania możesz wykorzystać pętlę z poprzedniego zadania, z tym, że:

analizujemy po 3 liczby na raz

zmienna sterująca przyjmie wartość od zera do ....?

3. Tym razem w wejściowej liście znajdują się napisy:
texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

Twoim zadaniem jest znalezienie takich par kolejnych napisów z tej listy, że długość pierwszego jest równa długości drugiego,
np, długość napisu "one" to 3, długość napisu "two" to 3, więc taka para powinna być odnaleziona. Z kolei długość napisu 'two' to 3,
a długość napisu "three" to 5, więc taka para nie jest rozwiązaniem. Właściwie można znowu bazować na poprzednich rozwiązaniach, ale:

zmieniła się tabela wejściowa

zmienia się warunek w if - to już nie są działania na liczbach ale porównywanie długości napisów'''


numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
max = len(numbers)-1
i=0

while i<max:
    print(numbers[i], numbers[i+1])

    if numbers[i]**2 == numbers[i+1]:
        print("\tFound: ", numbers[i], numbers[i+1])

    i+=1

print("---------------------------------------------------")
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
max = len(numbers)-2
i=0
while i<max:
    print(numbers[i], numbers[i+1], numbers[i+2])

    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:
        print("\tFound: ", numbers[i], numbers[i+1], numbers[i+2])

    i+=1
print("---------------------------------------------------")

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
max = len(texts)-1
i=0
while i<max:
    print(texts[i], texts[i+1])
    if len(texts[i]) == len(texts[i+1]):
        print("\tFound: ", texts[i], texts[i+1])
    i+=1

