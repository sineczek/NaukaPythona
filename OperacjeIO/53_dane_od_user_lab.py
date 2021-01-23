'''Teraz zajmiemy się rozwiązaniem równania kwadratowego. Te kilka wzorów może się przydać:


Przyda się również funkcja, która sprawdzi czy liczba jest całkowita (funkcja isdecimal() niespecjalnie mi się podoba, bo jej zdaniem liczby ujemne np. -1 nie jest liczbą całkowitą):

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


Aby rozwiązać zadanie należy:

zapytać użytkownika o współczynniki a,b i c

jeśli a lub b lub c nie są liczbami całkowitymi, to należy wyświetlić odpowiednią informację i zakończyć skrypt

w przeciwnym razie

należy sprawdzić czy a == 0

jeżeli tak, należy wyświetlić informację, że to nie jest równanie kwadratowe i zakończyć skrypt

w przeciwnym razie

należy wyliczyć deltę

jeżeli delta <0, to należy wyświetlić komunikat o braku rozwiązań i zakończyć skrypt

jeżeli delta=0,  to należy wyliczyć x1, wyświetlić wynik i zakończyć skrypt

jeżeli delta>0, to należy wyliczyć x1 i x2 , wyświetlić wynik i zakończyć skrypt

Po napisaniu skryptu przetestuj go z różnym danymi testowymi, np dla a, b i c:

3, 4, 1 - 2 rozwiązania:  -1 i -0.33

5, 4, -1 - 2 rozwiązania: -1 i 0.2

5, 4, 1 - brak rozwiązań

2, 0, 0 - jedno rozwiązanie: 0

0, 3, 4 - komunikat o tym, że a == 0

one, 1,1 - komunikat o tym, że a, b i c muszą być liczbami całkowitymi'''

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print('Ten skrypt rozwiąże równanie: ax^2+bx+c = 0')
print('Wprowadź wartości dla a, b oraz c:')

aStr = input('a=')
bStr = input('b=')
cStr = input('c=')

if not( check_int(aStr) and check_int(bStr) and check_int(cStr) ):
    print("a, b oraz c muszą być cyframi!")
else:
    a = int(aStr)
    b = int(bStr)
    c = int(cStr)

    if a == 0:
        print('To równanie kwadratowe! A nie może być 0!')
    else:
        delta = b**2 - 4*a*c

        if delta < 0:
            print("Brak rozwiązania")
        elif delta == 0:
            x1 = -b/(2*a)
            print("Jest jedno rozwiązanie: %.2f" % (x1))
        else:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("Są dwa rozwiązania: %.2f oraz %.2f" % (x1,x2))








