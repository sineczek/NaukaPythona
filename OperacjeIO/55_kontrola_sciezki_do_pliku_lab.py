'''Tym razem otrzymujesz zadanie zautomatyzowania pobierania danych dotyczących zamówień kierowanych z aptek do dystrybutora leków.
Zamówienia są przesyłane w postaci plików CSV  i umieszczane w katalogu c:\temp\data_input. Pliki są tam umieszczane przez różne inne procesy w ciągu całego dnia.
Codziennie o godzinie 19:00 będzie uruchamiany skrypt, który przeniesie te pliki do innego folderu, np c::\temp\yyyy-mm-dd
(gdzie yyyy to rok, mm to miesiąc, a dd to dzień z daty dzisiejszej). Potem na tych plikach są wykonywane dalsze operacje, jak np. import danych.

Obecnie skupimy sie na etapie sprawdzenia, czy wszystkie warunki do uruchomienia przetwarzania są spełnione, tzn.:

czy istnieje katalog wejściowy

czy istnieje katalog wyjściowy

czy NIE istnieje katalog odpowiadający dzisiejszej dacie

Ponieważ w szczególnym przypadku katalogu oznaczonego datą nie udałoby się utworzyć także wtedy, gdyby istniał plik o
takiej samej nazwie, to dodatkowo sprawdzimy też:

czy NIE istnieje plik odpowiadający dzisiejszej dacie

Zaimportuj moduł os i datetime

W zmiennej data_input_catalog zapamiętaj ścieżkę 'c:\temp\data_input'. Pamiętaj, że znak "\" ma specjalne znaczenie,
więc jeśli w ścieżce ma być zapisany rzeczywiście znak "\" - musisz użyć jakiegoś "chwytu")

W zmiennej data_output_catalog zapamiętaj ścieżkę 'c:\temp\data_output'

W zmiennej today zapisz dzisiejszą datę

Połącz ścieżkę znajdującą się w data_output_catalog z napisem w postaci ROK-MIESIAC-DZIEŃ wyliczoną w oparciu o  następujące wyrażenie (zresztą baaardzo przydatne):

today.strftime("%Y-%m-%d")

Wynik zapisz w zmiennej today_output_catalog

W zmiennej is_input_catalog_ok zapisz wynik testu sprawdzającego czy katalog data_input_catalog ISTNIEJE i jest katalogiem

W zmiennej is_output_catalog_ok zapisz wynik testu sprawdzającego czy katalog data_output_catalog ISTNIEJE i jest katalogiem

W zmiennej is_today_output_catalog_ok zapisz wynik testu sprawdającego czy ścieżka today_output_catalog NIE ISTNIEJE ani jako plik ani jako katalog

Jeżeli wynik wszystkich 3 wyżej wymienionych testów jest poprawny, to wyświetl komunikat 'Conditions met! We can continue!'

W przeciwnym razie wyświetl komunikat o błędzie, a następnie w zależności od wartości logicznej zmiennych is_...._ok
wyświetl, co dokładnie jest nie tak (np brak katalogu input lub output itp)

Przetestuj działanie skryptu w różnych warunkach, np.:

wszystko jest ok

brak katalogu wejściowego lub wyjściowego (lub obu  na raz)

plik o nazwie odpowiadającej dzisiejszej dacie istnieje

itp.'''

import os
import datetime

data_input_catalog = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'
today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))
is_input_catalog_ok = os.path.isdir(data_input_catalog) and os.path.exists(data_input_catalog)
is_output_catalog_ok = os.path.isdir(data_output_catalog) and os.path.exists(data_output_catalog)
is_today_output_catalog_ok = not os.path.isdir(today_output_catalog) and not os.path.isfile(today_output_catalog)

print('Dir Input: ', data_input_catalog, '\nDir Output: ', data_output_catalog, '\nDate: ', today, '\nDir for today: ',
      today_output_catalog, '\nIs input catalog ok? ', is_input_catalog_ok, '\nIs output catalog ok?',
      is_output_catalog_ok, '\nIs today output catalog ok?', is_today_output_catalog_ok,
      '\n-----------------------------------------\n')

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Conditions NOT met! Check the paths!')

    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % data_input_catalog)
    if not is_output_catalog_ok:
        print("Output catalog %s must exist!" % data_output_catalog)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)
