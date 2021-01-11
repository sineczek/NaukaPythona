'''ZADANIE 1

Dana jest lista:

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
Napisz pętlę for, która wyświetli elementy tej listy jeden po drugim. Podczas wyświetlania elementów konwertuj napisy do wielkich liter.'''

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for x in data:
    print(x.upper())
else:
    print('---------------------\n---------------------')


'''ZADANIE 2

Jak widzisz, każdy z elementów listy zawiera znak ":".

W pętli for każdy z przetwarzanych napisów rozbij ze względu na ":" korzystając z funkcji split.

Wynik zapamiętaj w nowej dwuelementowej liście elements.

Następnie wyświetl elements[0] konwertując napis do wielkich liter, a elements[1] wyświetl bez żadnej konwersji'''
elements = []

for x in data:
    elements = x.split(':')
    print(elements[0].upper())
    print(elements[1])
print('---------------------\n\n---------------------')



'''ZADANIE 3

Rozpocznij od poprzednio utworzonej pętli. Zmieniamy zasady wyświetlania:

Jeżeli w elements[0] znajduje się napis "Error", wyświetl elements[1] konwertując tekst do wielkich liter

w przeciwnym razie wyświetl elements[1] bez żadnej konwersji
'''
for x in data:
    elements = x.split(':')
    if elements[0] == "Error":
      print(elements[1].upper())

    else:
      print(elements[1])



print('---------------------\n---------------------')


