'''ZADANIE 1
Nadal pracujemy nad tymi samymi funkcjami, co poprzednio. Zaczynamy od funkcji PrintAnimal.
Należy zwrócić informację o tym czy obrazek został wyświetlony, czy nie:

Jeżeli przekazano poprawny parametr i obrazek został wyświetlony, należy zwrócić wartość True

Jeżeli przekazano niepoprawny parametr i obrazek nie został wyświetlony, należy zwrócić False

Przetestuj działanie funkcji po zmianie'''
def PrintAnimal(pet=''):
    # this function prints a cat, bear or bat ascii-art
    wasPrinted = ''
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
        wasPrinted = True
        print(txt_cat, '\n ASCII-Art was printed:',wasPrinted)

    elif pet == 'bear':
        wasPrinted = True
        print(txt_bear, '\n ASCII-Art was printed:',wasPrinted)

    elif pet == 'bat':
        wasPrinted = True
        print(txt_bat, '\n ASCII-Art was printed:',wasPrinted)

    elif pet == '':
        wasPrinted = False
        print('Podaj zwierze.', '\n ASCII-Art was printed:',wasPrinted)

    else:
        wasPrinted = False
        print("Brak '%s'w zwierzyńcu. możesz wybrać: cat, bear, bat" % pet, '\n ASCII-Art was printed:',wasPrinted)

    return


PrintAnimal('cat')
PrintAnimal(pet='bear')
PrintAnimal(pet='bat')
PrintAnimal('unicorn')
PrintAnimal()

print('-------------------------------- \n \n rozwiązanie z ćwiczenia:')
def PrintAnimal(animal = ''):
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

    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
        return False

    return True


if PrintAnimal():
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')


if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')


if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
'''ZADANIE 2
Teraz modyfikujemy funkcję DaysToEndOfYear. Ilość dni do Sylwestra nie ma być wyświetlana, ale zamiast tego zwracana. 
Przetestuj działanie funkcji'''

print('------------------------\n')
from datetime import date
def DaysToEndOfYear(year=date.today().year, \
                    month=date.today().month, \
                    day=date.today().day):


    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days


print('Date: 2021-12-20 days to end of year: %d' %( DaysToEndOfYear(2021,12,20)))
print('Date: 2021-12-21 days to end of year: %d' %( DaysToEndOfYear(2021,12,21)))
print('Date: 2022-12-22 days to end of year: %d' %( DaysToEndOfYear(year = 2022, month = 12, day = 22)))
print('Date: 2023-1-21 days to end of year: %d' %( DaysToEndOfYear(day = 21, month =1, year = 2023)))
print('Date: TODAY days to end of year: %d' %( DaysToEndOfYear()))


