'''1. Zaimportuj modul time

2. Wyświetl czas (datę i godzinę) w postaci Unix Epoche (skorzystaj z metody time)

3. Wyświetl czas (datę i godzinę) w postaci czytelnej dla człowieka. W tym celu złóż metodę localtime z metodą time

4. Zaimportuj moduł calendar

5. Każdy z nas ma swoje ważne daty: datę urodzenia swoją, dziewczyny/chłopaka, dziecka, data przyjęcia do pierwszej pracy, data zakończenia podstawówki itp.
Wyświetl miesiąc zawierający tą datę

6. Zmień sposób wyświetlenia daty tak, aby niedziela była pierwszym dniem tygodnia

7. Wyświetl miesiąc z ważną dla Ciebie datą ponownie

8. Sprawdź czy rok 2000 był przestępny

9. Wyświetl kalendarz za rok 2019 i zobacz czy układ świąt Bożego Narodzenia wygląda atrakcyjnie czy nie'''

#1.
import time
#2.
print('Unix epoch style:',time.time())
#3.
print('For humanz:',time.asctime())
#4.
import calendar
#5.
print('Dzień boga w kalendarzu:', calendar.month(1981,3))
#6.
calendar.setfirstweekday(6)
#7.
print('Dzień boga w kalendarzu:', calendar.month(1981,3))
#8.
print('czy rok 2k był przestępny?',calendar.isleap(2000))
#9.
print(calendar.calendar(2019))





