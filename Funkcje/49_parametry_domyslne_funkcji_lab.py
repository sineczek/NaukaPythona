'''ZADANIE 1
Nadal kontynuujemy pracę nad poprzednio tworzonymi funkcjami. Funkcja PrintAnimal(animal) wyświetla obrazek
odpowiadający przekazanemu parametrowi. A co jeśli żaden parametr nie zostanie przekazany? Obecnie funkcja wyświetli błąd.

Zmień to. Jeżeli żaden parametr nie został przekazany, to parametr animal ma być zainicjowany napisem pustym.
Po zmianie wywołaj funkcję przekazując parametr lub go opuszczając. W przypadku opuszczenia parametru powinien zostać
wyświetlony komunikat wskazujący na poprawne wartości parametru.'''

def PrintAnimal(pet=''):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''

    if pet == 'cat':
        print(txt_cat)
    elif pet == 'bear':
        print(txt_bear)
    elif pet == 'bat':
        print(txt_bat)
    elif pet == '':
        print('Podaj zwierze.')
    else:
        print("Brak '%s'w zwierzyńcu. możesz wybrać: cat, bear, bat" % pet)

    return


PrintAnimal('cat')
PrintAnimal(pet='bear')
PrintAnimal(pet='bat')
PrintAnimal('unicorn')
PrintAnimal()


'''ZADANIE 2
Funkcja DaysToEndOfYear(year, month, day) z poprzeniego laboratorium też wymaga drobnej poprawki

Jeżeli któryś z parametrów został opuszczony podczas wywołania, to należy podstawić rok, miesiąc lub dzień z daty dzisiejszej. 
Przetestuj wywołanie funkcji na różne sposoby

Uwaga! Ponieważ operacje na dacie trzeba wykonać jeszcze przed samą definicją funkcji (mówimy o tym "w sygnaturze funkcji"), 
to polecenie importujące moduł datetime trzeba przesunąć z definicji funkcji (ciała funkcji) na początek skryptu. Pozwoli to na korzystanie z funkcji date.today()'''

print('------------------------\n')
from datetime import date
def DaysToEndOfYear(year=date.today().year,\
                    month=date.today().month,\
                    day=date.today().day):


    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)

DaysToEndOfYear(2021,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 21, month =1, year = 2023)
DaysToEndOfYear()
