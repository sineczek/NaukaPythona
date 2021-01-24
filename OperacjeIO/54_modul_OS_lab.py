'''Uwaga: w najbliższych lekcjach i zadaniach będziemy pracować z plikami. Będzie znacznie bezpieczniej, jeśli nie będziesz wtedy pracować w katalogu systemowym i nie będziesz wskazywać ścieżki do plików systemu operacyjnego. Jeśli coś  pójdzie nie tak unikniesz w ten sposób uszkodzenia systemu operacyjnego. Najlepiej będzie założyć sobie specjalny katalog z kilkoma podkatalogami i wkopiować do nich kilka plików. Jeśli utracisz ten katalog, żadnych strat nie będzie!

1. Zaimportuj moduły os i time

2. Poproś użytkownika o wprowadzenie ścieżki dostępu do katalogu i zapisz pobrany napis w zmiennej dir

3. Jeśli wprowadzony napis nie wskazuje na katalog, wyświetl komunikat i zakończ skrypt

4. W przeciwnym razie poproś użytkownika o wprowadzenie nazwy pliku i zapisz pobrany napis w zmiennej file

5. Korzystając z odpowiedniej funkcji modułu os połącz ze sobą katalog z plikiem tworząc pełną ścieżkę. Wynik zapamiętaj w zmiennej path

6. Jeżeli plik wskazywany przez path nie istnieje, wyświetl komunikat i zakończ skrypt

7. Wyświetl informację o tym, że poniżej będą wyświetlane właściwości pliku path, a potem wyświetl:

datę ostatniej modyfikacji

rozmiar w bajtach

informację o biżącym katalogu

ścieżkę względną do pliku'''

import os
import time


dir = input('Podaj ścieżkę do katalogu: ')
if os.path.isdir(dir):
    print('Dziękuje. Podana ścieżka do katalogu to: ', dir)
    file = input('Podaj nazwę pliku: ')
    path = os.path.join(dir,file)

    if os.path.exists(file):
        print('Podana pełna ścieżka do pliku to: ',path,'\nPoniżej informacje o pliku %s.' % os.path.basename(path))
        print('\nData ostatniej modyfikacji: ',time.localtime(os.path.getmtime(path)))
        print('\nRozmiar pliku: ', os.path.getsize(path),'b')
        print('\nPlik znajduje się w katalogu: ',os.path.dirname(path))
        print('\nWzględna ścieżka do pliku: ', os.path.relpath(path))
    else:
        print('Plik nie istnieje! Utwórz go i spróbuj ponownie.')



else:
    print('To miała być ścieżka do katalogu!')







