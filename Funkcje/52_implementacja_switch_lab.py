'''Budujemy moduł służący do obliczeń na ciągach geometrycznych

ZADANIE 1

Zaimportuj moduł math

Przygotuj funkcję GiveGeomSeqElement, która:
-przyjmuje 3 parametry a1 - o domyślnej wartości  2, która oznacza pierwszy element ciągu, factor - o domyślnej wartości 2,
 która oznacza współczynnik ciągu geometrycznego, index o domyślnej wartości 2, która oznacza  który element ciągu ma być wyliczony
-dodaj do funkcji komentarz, który opisze co robi ta funkcja
-wylicz wartość ciągu. Odpowiedni wzór znajdziesz np tu: https://pl.wikipedia.org/wiki/Ci%C4%85g_geometryczny

Wylicz wartość 64 elementu ciągu geometrycznego, którego pierwszym elementem jest 1 a współczynnik wynosi 2

ZADANIE 2

Przetestuj działanie funkcji. Napisz pętlę for, która wyznaczy i wyświetli elementy a1, a2, a3,...a10 dla ciągu geometrycznego
 o pierwszym wyrazie równym 3, współczynniku 2

Wskazówki:
-zadeklaruj a1=3, factor=2 i maxindex=10
-napisz pętlę for, gdzie wartość sterująca pętli nazywa się i i zmienia się od 1 do maxindex
-dla każdej wartości wyliczy wartość elementu korzystając z funkcji

ZADANIE 3

Przygotuj funkcje GiveFactorForGeomSeq, która wyznaczy wartość współczynnika gdy znane są 2 kolejne wyrazy ciągu.

Wskazówki:
-Funkcja ma mieć 2 parametry term i nextterm bez wartości domyślnej
-dodaj komentarz o funkcji
-Aby uzyskać wartość podziel nextterm przez term i zwróć wynik

Przetestuj działanie funkcji dla 12 i 24

ZADANIE 4

Utwórz funkcję GiveSumOfNElementsGeomSeq, która wyznaczy sumę pierwszych wyrazów ciągu.

Funkcja ma:
-przyjąć parametr a1 o domyślnej wartości 2, która oznacza pierwszy wyraz ciągu, factor o domyślnej wartości 2,
która oznacza współczynnik ciągu i n oznaczające ile pierwszych elementów ciągu ma być dodanych. Domyślna wartość tego praramertu to 2
-wzór na sumę znajdziesz pod adresem: https://pl.wikipedia.org/wiki/Ci%C4%85g_geometryczny

Przetestuj działanie funkcji wyliczając sumę dla ciągu o pierwszym elemencie równym 2, współczynnikiem 3 dla pierwszych 4 elementów

ZADANIE 5

Przenieś wszystkie funkcje i linijkę importującą moduł math do nowego pliku. Zapisz go pod nazwą geom.py

W pliku skryptu zaimportuj  moduł geom

Zmień instrukcje wywołujące funkcje, aby korzystały z funkcji modułu (dodaj prefix geom. )

Uruchom skrypt i przetestuj funkcje, które zostaną zaimportowane z modułu geom.'''
#ZADANIE 1
import math
def GiveGeomSeqElement(a1=2,\
                   factor=2,\
                   index=2):
    # ciąg liczbowy (skończony bądź nieskończony), którego każdy kolejny wyraz od drugiego począwszy jest iloczynem wyrazu poprzedniego i pewnej stałej nazywanej ilorazem ciągu. Ciąg geometryczny można traktować jako multiplikatywną wersję ciągu arytmetycznego.
    value = a1*pow(factor,index-1)
    return value
print('Wynik dla 3,3,3 to:',GiveGeomSeqElement(3,3,3))
print('Wynik dla 2,2,2 to:',GiveGeomSeqElement())
print('Wynik dla 1,2,64 to:',GiveGeomSeqElement(1,2,64))

print('------------------------------------------------')

#ZADANIE 2
a1=3
factor=2
maxindex=10
for i in range(1,maxindex):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
print('------------------------------------------------')

#ZADANIE 3
def GiveFactorForGeomSeq(term,nextterm):
    #ciąg liczbowy (skończony bądź nieskończony), którego każdy kolejny wyraz od drugiego począwszy jest iloczynem wyrazu poprzedniego
    #i pewnej stałej nazywanej ilorazem ciągu. Ciąg geometryczny można traktować jako multiplikatywną wersję ciągu arytmetycznego.
    #znane 2 kolene wyrazy ciągu
    return nextterm/term
print('Factor is', GiveFactorForGeomSeq(12,24))

#ZADANIE 4
def GiveSumOfNElementsGeomSeq(a1=2,factor=2,n=2):
    #zwraca sumę
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN
print('Sum of n elements is', GiveSumOfNElementsGeomSeq(2,3,4))

#ZADANIE 5
'''Przenieś wszystkie funkcje i linijkę importującą moduł math do nowego pliku. Zapisz go pod nazwą geom.py

W pliku skryptu zaimportuj  moduł geom

Zmień instrukcje wywołujące funkcje, aby korzystały z funkcji modułu (dodaj prefix geom. )

Uruchom skrypt i przetestuj funkcje, które zostaną zaimportowane z modułu geom.'''




