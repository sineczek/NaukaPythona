'''W tym zadaniu będziemy przetwarzać plik orders.csv z zamówieniami z apteki. Zacznij od zapisania w pliku następujących danych:

Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10
Załóżmy, że ten tekst został umieszczony w pliku c:\temp\data_input\orders.csv

Naszym zadaniem jest przeczytać ten plik i przetwarzać go linijka po linijce. Zamówienie umieszczone w każdej linii składa się
z 3 informacji: nazwa apteki, nazwa leku, ilość opakowań leku. Zdarza się, że niektóre zamówienia nie są poprawne i zawierają
więcej danych - tutaj wiersz 2. W tym zadaniu przetwarzamy ten plik zupełnie ręcznie, ale oczywiście istnieją zdecydowanie
lepsze metody na przetwarzanie danych w Pythonie, np. biblioteka PANDAS, której poświęciłem inny kurs.

Ale po kolei:

1. W zmiennej file_path zapisz ścieżkę dostępu do pliku (uważaj na znaki \)

2. Wybraną przez siebie metodą otwórz plik i przetwarzaj go  linijka po linijce

3. Każda wczytana linijka kończy się znakiem ENTER. Usuń go.

3. Rozbij linijkę ze względu na znak przecinka. Wynik (lista pól opisujących zamówienie) zapisz w zmiennej order

4. Jeśli lista order ma dokładnie 3 elementy, to: wyświetl komunikat 'Order from drugstore "%s", item "%s", amount %s'
zastępując %s kolejnymi elementami listy order

5. Jeśli lista order ma inną ilość elementów, to wyświetl komunikat "Line %s malformed!!!" , zamieniając %s na zawartość tej linijki

6. Na zakończenie wyświetl informację o zakończonym przetwarzaniu i zależnie od wybranej metody przetwarzania pliku - zamknij plik jeśli trzeba

'''

file_path = 'c:\\temp\\input_data\\orders.csv'

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace('\n','')
        order = line.split(',')
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' % (order[0],order[1],order[2]))
        else:
            print('Line %s malformed!!!' % (order))

print('All done! Thank You, Come again!')



