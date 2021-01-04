'''
Zadania:
1. Wyświetl tekst napisany tylko wielkimi literami
2. Wyświetl tekst zapisany tylko małymi literami
3. Sprawdź czy tekst kończy się słowem 'street'
4. Sprawdź czy tekst jest zapisany wielkimi literami
5. Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
6. Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'
7. Zamień w tekście słowo 'one' na '1'
8. Zamień w tekście słowo 'one' na '1' a słowo 'both' na 2
9. Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja
10. Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
'''

#1.
quote='A good programmer is someone who always looks both ways before crossing a one-way street'
#2.
print(quote.upper())
#3.
print(quote.endswith('street'))
#4.
print(quote.isupper())
#5.
print(quote.upper().isupper())
#6.
print(quote.find('one'))
#7.
print(quote.replace('one', '1'))
#8.
print(quote.replace('one', '1').replace('both', '2'))
#9.
print(quote.split(' '))
#10.
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())