'''nie ma takiej stałej :( trzeba zainportować moduły math
print(pi)
print(math.pi)'''

#ta metoda jest lepsza dla scryptów
import math
print(math.pi)
print(math.floor(math.pi)) #zaokrąglanie

#przy tak zaimportowanym module zawsze jednak trzeba wskazać moduł
#trzeba zawsze zaimportować po restarcie shella


#ta metoda lepsza jak piszemy z interakcjami (i komendy się nie poeiwlaja)
from math import *
print(pi)
#jak się tak zaimportuje nie trzeba używac nazwy modułu
#trzeba uważać bo czasem funckje mają tą samą nazwę
#math.pi teraz nie zadziała!



