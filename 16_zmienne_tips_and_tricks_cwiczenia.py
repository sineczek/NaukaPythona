'''
1. Zadeklaruj zmienne:
v1 o wartości 126
v2 o wartości '126'
v3 o wartości 126.0
v4 o wartości '126.0'

2. Zastanów się (na razie bez sprawdzania), jaki typ mają te zmienne

3. Poleceniami print wyświetl wartości zmiennych i ich typ. Dobrze odgadłeś(aś) typ zmiennych?

4. Poleceniami print wyświet:

wynik dodawania v1 i v3 oraz typ tak wyznaczonego wyniku

wynik dodawania v2 i v4 oraz typ tak wyznaczonego wyniku

5. Ile to jest:

7-1*0+3+3

Najpierw policz w pamięci, a potem z Pythonem

6. Ile to jest  4 do potęgi piątej podzielone przez 2 do potęgi 3

7. To zadanie to raczej matematyczna łamigłówka, niż typowe zadanie z Pythona, ale z drugiej strony to "smaczek"
bycia programistą lub matematykiem...

Wyobraż sobie, że zepsuła Ci się klawiatura. Działa tylko klawisz 9, klawisze z działaniami +-*/ oraz klawisze nawiasów
i enter. Na dodatek klawisz 9 możesz nacisnąć tylko maksymalnie 4 razy, bo po kolejnym naciśnięciu.... komputer się restartuje.

Twoim zadaniem jest napisanie na tej zepsutej klawiaturze w interpreterze Python takiego działania, aby jego wynik wynosił 100

'''

v1 = 126 #int
v2 = '126' #str
v3 = 126.0 #float
v4 = '126.0' #str

print(type(v1))
print(type(v2))
print(type(v3))
print(type(v4))

print(type(v1 + v3))
print(type(v2 + v4))

print(7-1*0+3+3)

print((4**5)/(2**3))
print(4**5/2**3)
print((4**5)/2**3)

print(99+9/9) #HA ! ciekawe czy dobrze

