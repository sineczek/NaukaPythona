'''ZADANIE 1

Nadal poprawiamy znane Ci funkcje. Zaczynamy od PrintAnimal.

Zmień definicję funkcji tak, aby można było przekazać zmienną ilość nazw zwierząt, które mają być narysowane.
Na tym etapie rezygnujemy ze zwracania wartości oraz wartości domyślnej. Po zmianach przetestuj działanie funkcji
przekazując po kilka nazw zwierząt jako parametr (wybieraj spośród tych zdefiniowanych w funkcji, jak i niepoprawnych)'''


def PrintAnimal(*pets):
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

    for pet in pets:
        if pet == 'cat':
            print(txt_cat)
        elif pet == 'bear':
            print(txt_bear)
        elif pet == 'bat':
            print(txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % pet)

    return


PrintAnimal('cat', 'dog')
PrintAnimal('unicorn', 'bat')
PrintAnimal()
PrintAnimal('cat', 'bat', 'dog', 'bear')
print('-------------------------------------\n')

'''ZADANIE 2

A teraz kolej na DaysToEndOfYear:

zmień parametr tak, aby przyjmował wiele dat (uwaga funkcja będzie przyjmować daty, a nie osobne wartości rok/miesiąc/dzień)

dla każdej daty z parametrów ma zostać wyświetlona informacja o dacie i ilości dni do Sylwestra

usuń część funkcji odpowiadającą za zwracanie wartości

przetestuj działanie funkcji przekazując różną ilość argumentów'''


from datetime import date

def DaysToEndOfYear(*dates):

    for date_today in dates:

        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)

DaysToEndOfYear(date(1999,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2019,1,5))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,25),date(2021,1,23))
print('----------------')
