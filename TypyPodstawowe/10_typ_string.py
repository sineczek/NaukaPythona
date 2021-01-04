#typ zmiennej string - czyli napis
atext='This is a text.'
atext.endswith('ext') #xzy kończy się na ext

atext.endswith('ext.')

atext.islower() #czy małymi literami

atext.upper().isupper() # przekształciła na duże i sprawdziła czy jest dużymi

atext.find('is') # czy np. występuje coś i w którym miejscu, ale tylko pierwsze wystąpienie, a python liczy od 0

atext.find('is',3) # od trzeciego znaku ma szukać

atext.replace('a', 'b') #zamieni a na b w texcie

atext.replace('a', '4').replace('i','1') #zamieni a na 4 oraz i na 1

atext.split(' ') # podział textu w miejscu spcji i umieszczenie w tabelii

'''
    do textu nie można dodawać cyfr, nawet jak cyfry są w formie '100' np.
    cyfraJakoText='100'
    cyfraJakoText+1 
    spowoduje to komunikat z błedem
'''
cyfraJakoText='100'
cyfraJakoText.isdigit() #sprawdza czy string jest cyfrą True/False

cyfraJakoText.isdecimal() #czy ma przeicnek

cyfraJakoText.isalpha() #czy jest z samych liter

cyfraJakoText.isalnum() #czy jest alfanumeryczna








