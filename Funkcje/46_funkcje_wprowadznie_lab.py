'''Przygotowujesz skrypty, które nie tylko wykonają pewne czynności, ale dodatkowo wygenerują raport,
który będzie oznaczony logo firmy. Naszym logo będzie kot, miś lub nietoperz.

Napisz funkcje:

PrintCat() - wyświetlającą kota

PrintBear() - wyświetlającą misia

PrintBat() - wyświetlającą nietoperza.

Oto dane, które przydadzą się w tym zadaniu:




(więcej fajnych obrazków znajdziesz np tu: https://www.asciiart.eu/'''

def PrintCat():
    #druk kota
    print('''
|\---/|
| o_o |
 \_^_/''')
    return

def PrintBear():
    #druk misia
    print('''
/  \.-"""-./  \\
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`''')
    return


def PrintBat():
    #druk nietoperka
    print('''
   /\\                 /\\
  / \\'._   (\_/)   _.'/ \\
 /_.''._'--('.')--'_.''._\\
 | \_ / `;=/ " \=;` \ _/ |
  \\/ `\\__|`\\___/`|__/`  \\/
          \\(/|\\)/       ''')
    return


PrintBat()
PrintCat()
PrintBear()

print('--------------- z przykładu \n')

def PrintCat():
    # this function prints a cat ascii-art
    txt = r'''
|\---/|
| o_o |
 \_^_/'''
    print(txt)
    return

def PrintBear():
    # this function prints a bear ascii-art
    txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    print(txt)
    return

def PrintBat():
    # this function prints a bat ascii-art
    txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
    print(txt)
    return


PrintCat()
PrintBear()
PrintBat()
