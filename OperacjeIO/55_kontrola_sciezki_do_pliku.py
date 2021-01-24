import os
#trochę zmodyfikowany skrypt

f = 'results.txt'

while True:
    path = input('Wprowadź ścieżkę do pliku %s: ' %(f))
    filename = os.path.join(path,f)
    if os.path.isfile(filename):
        break
    else:
        print('Lokalizacja pliku %s jest niepoprawna. Spróbuj ponownie.' % (f))

print('Plik %s znajduje się w %s' % (f, os.path.dirname(filename)))