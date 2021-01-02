'''
1. Zadeklaruj zmienną helloMessage i wpisz do niej tekst:

"Hello %s!"
'''
helloMessage = "Hello %s"



#2. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa powitania: raz %s należy zamienić na Kate a raz na Chirs
print(helloMessage % "Kris")
print(helloMessage % "Kate")


'''3. Zmień zawartość zmiennej helloMessage na

"Hello {0:s}!"
'''

helloMessage2 = "Hello {0:s}"

#4. Podobnie , jak w punkcie drugim wyświetl powitanie z Kate i Chis, ale tym razem skorzystaj z metody format
print(helloMessage2.format("Kate"))
print(helloMessage2.format("Kris"))

'''5. Zmień zawartość zmiennej helloMessage na

"%s has %d %s"
'''
message1 = "%s has %d %s"

'''6. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa komunikaty
w pierwszym komunikacie %s zamień na Kate, %d na 1, a %s na animal
w drugim komunikacie %s zamień na  Chris, %d na 100000, a %s na $
'''
print(message1 % ("Kate", 1,"animal"))
print(message1 % ("Chris",100000,"$"))

'''7. Zmień zawartość zmiennej helloMessage na

"{0:s} has {1:d} {2:s}"
'''
message2 = "{0:s} has {1:d} {2:s}"

#8. Wyświetl te same komunikaty, jak w punkcie 6, ale tym razem skorzystaj z metody format
print(message2.format("Kate", 1, "animal"))
print(message2.format("Chris", 100000, "$"))

'''
9. [Trochę trudniejsze, ale cała trudność polega na samodzielnym zbudowaniu napisu formatującego i to w takiej postaci, 
że na każdy element w napisie ma zostać przewidziana określona liczba znaków]
Utwórz zmienną line i wpisz do niej tekst pozwalający na wyświetlenie na 20 znakach pewnego napisu, następnie słowa 
"costs", następnie na 6 znakach pewnej liczby i następnie znaku €, np:

ICE CREAM            costs      3 €
TRIP TO VENICE       costs    119 €
PIZZA HAWAII         costs      6 €
... BTW, wiesz jak uzyskać znak € z klawiatury? O ile używasz Windows powinien zadziałać prawy ALT + u
'''
line = "{0:20s} cost {1:6d} €"


'''10. Korzystając ze zmiennej line i polecenia print,  zamieniaj odpowiednie znaczniki na podane niżej wartości, tak aby w efekcie został wyświetlony cennik usług:

ICE CREAM    3

TRIP TO VENICE  119

PIZZA HAWAI  6'''

print(line.format("ICE CREAM", 3))
print(line.format("TRIP TO VENICE", 119))
print(line.format("PIZZA HAWAII", 6))