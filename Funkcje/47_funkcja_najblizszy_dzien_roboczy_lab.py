'''Kto się lubi bawić w Sylwestra? Ręka do góry!

Przygotujmy funkcję, która wyświetli ile dni zostało do końca roku. Jeśli wiesz jak to zrobić to nie czytaj dalej, a jeśli chcesz pewnych wskazówek - oto one:

najpierw napisz skrypt, potem skonwertujesz go do funkcji

zaimportuj z modułu datetime typ date

korzystając z funkcji today() z modułu date zapisz w zmiennej date_today datę dzisiejszą

korzystając z odpowiedniej właściwości zmiennej date_today pobierz rok z tej daty do zmiennej current_year

do zmiennej date_end_year zapisz datę zbudowaną z current_year, 12 (grudzień) i 31 (Sylwester). Skorzystaj z metody date, do której przekażesz te zmienne

do zmiennej delta zapisz różnicę między date_end_year i date_today

wyświetl ilość dni z obiektu delta. Skorzystaj z odpowiedniej właściwości

sprawdź działanie skryptu

skonwertuj skrypt na funkcję

sprawdź działanie funkcji wywołując ją

No to dużo jeszcze do Sylwestra?'''




def DaysToEndOfYear():
    import datetime

    today = datetime.date.today()
    currentYear = today.year
    newYearsEve = datetime.date(currentYear, 12, 31)
    ilosc = newYearsEve - today

    print('do Nowego Roku pozostało:', ilosc.days, 'dni')
    return

DaysToEndOfYear()