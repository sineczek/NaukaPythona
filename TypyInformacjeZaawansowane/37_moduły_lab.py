'''Oto lista wyników konkursu Eurowizja 2018:

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

W statystyce można posługiwać się pojęciem mediany. Mediana to "wartość środkowa".
Dokładnie połowa elementów zbioru ma być mniejsza od mediany i dokładnie połowa elementów ma być większa od mediany.
Z wyliczeniem mediany nie ma problemu jeżeli ilość elementów zbioru jest nieparzysta.
Jeśli ilość elementów zbioru jest parzysta, to przyjmuje się, że mediana jest równa średniej wartości znajdujących się w środku zbioru.

Nasz zbiór ma 26 elementów, co jest liczbą parzystą. Będziemy szukać wartości, która znajdzie się między 13, a 14 elementum zbioru po posortowaniu
(a dokładniej średniej z elementu 13-go i 14-go) .

Mamy też do dyspozycji funkcje median_low, która zwróci wartość elementu 13-go i funkcję median_high, która zwróci wartość elementu 14-go.

Najpierw posortuj listę i wyświetl ją.

Teraz spóbuj wywołać metodę median przekazując do niej jako argument listę percent. (powinien pojawić się komunikat o błędzie)

Podobnie wywołuje się metodę median_low i median_high (ale tu również będzie błąd)

Zaimportuj modul statistics

Wylicz median, median_low i median_high, poprzedzając nazwy funkcji słowem "statistics" i kropką (teraz wszystko powinno zadziałać, bo moduł jest zaimportowany)

Zaimportuj do sesji pythona wszystkie funkcje tak, aby nie trzeba było ich poprzedzać nazwą modułu

Wywołaj metody median, median_low i median_high bez poprzedzania ich nazwą modułu (teraz wszystko powinno zadziałać,
bo funkcje z modułu statistics zostały zaimportowane bezpośrednio do nazw rozpoznawanych przez python)'''

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]
percent.sort()
print(percent)
print('\n')
import statistics

print('Mediana:',statistics.median(percent), '\tMediana LOW:', statistics.median_low(percent), '\tMedian HIGH', statistics.median_high(percent))

from statistics import median, median_high, median_low
print('Mediana:',median(percent), '\tMediana LOW:', median_low(percent), '\tMedian HIGH', median_high(percent))













