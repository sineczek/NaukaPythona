line = 'this IS a Very STRANGE text'
print(line.capitalize()) #zdanie z dużej litery, reszta mała

print(line.title()) #każde słowo z dużej litery

print(line.upper()) #wszystko dużymi
print(line.lower())

print(line.swapcase()) #to co było dużymi jest z małych i na odwrót

line = 'der Fluss verästelt sich hier fig'
print(line.casefold()) #zamienia np ß na ss, w polskim nie działa

line = 'ŻÓŁĆ'
print(line.lower())
print(line.casefold())

print(line.replace('Ż','Z').replace('Ó','O').replace('Ł','L').replace('Ć','C'))

line = 'this IS a Very STRANGE text'
print(line.count('e'))
print(line.find('e')) #od lewej
print(line.rfind('e')) #od prawej
print(line.index('e'))
print(line.rindex('e'))

print(line.find('p')) #-1
#print(line.index('p')) #błąd

import string
print(string.ascii_letters)
print(string.digits)

print(line.split(' ')) #rozbija na listę
list=line.split(' ')
print(' '.join(list)) #połaczenie listy


