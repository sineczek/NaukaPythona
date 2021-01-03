'''
Zadania:
1. Wyświetl tekst napisany tylko wielkimi literami
2. Wyświetl tekst zapisany tylko małymi literami
3. Sprawdź czy tekst kończy się słowem 'street'
4. Sprawdź czy tekst jest zapisany wielkimi literami
5. Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
6. Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'
7. Zamień w tekście słowo 'one' na '1'
8. Zamień w tekście słowo 'one' na '1' a słowo 'both' na 2
9. Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja
10. Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
'''
#typy string
text = "A good programmer is someone who always looks both ways before crossing a one-way street"
print(text.upper())
print(text.lower())
print(text.endswith("street"))
print(text.isupper())
print(text.upper().isupper())
print(text.find("one"))
print(text.replace("one", "1"))
print(text.replace("one", "1").replace("both", "2"))
print(text.split(" "))
print(text.isdigit())
print(text.isdecimal())
print(text.isalpha())
print(text.isalnum())
'''
1. Pracujesz w Urzędzie Stanu Cywilnego i ... korzystasz z Pythona. Dziewczyna o imieniu Kasia i nazwisku Sowa wychodzi za mąż za chłopaka o nazwisku Mrugała.
Pani Kasia chce zachować oba nazwiska.

Zdefiniuj zmienne firstName, famillyName i famillyName i przypisz do nich napisy odpowiadające imieniu, nazwisku panieńskim i nowym nazwisku.
Następnie utwórz zmienną newName i zapisz w niej wynik konkatenacji (czyli złączenia napisów) dla firstname, spacji, familyName, spacji i lastName.
Wyświetl to nowe nazwisko

2. Zdefiniuj zmienną music o następującej zawartości (są to tytuły i autorzy piosenek z filmu Minionki):

"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I'm a Man" Steve Winwood

Uwaga! Ten napis zawiera zarówno apostrof jak i cudzysłów, więc musisz zmodyfikować zapis metodami pokazanymi na tej lekcji, żeby zdefiniowanie zmiennej się udało.

3. W powyższym tekście mowa jest o 3 piosenkach. Zmień tekst tak, aby druga i trzecia piosenka podczas wyswietlania były umieszczone w nowej linii (znowu musisz w tekście dodać pewne znaki specjalne prezentowane na lekcji).

4. Przygotuj kilka poleceń print, które wyświetlą taki oto ascii art:

(\(\
( -.-)
O_(")(")

 Czy wiesz, że twórca języka Python - Guido Van Rossum - był fanem latającego cyrku Monty Pythona? Tak. To od tego wzięła się nazwa języka!
'''
#konkatacja napisów
firstName = "Kasia"
famillyName = "Sowa"
famillyName2 = "Mrugała"

newName = firstName + " " + famillyName + " " + famillyName2
print(newName)

music = '"Universal Fanfare" Jerry Goldsmith \n"Happy Together" Garry Bonner \n"I\'m a Man" Steve Winwood'
print(music)

print('(\\(\\')
print('( -.-)')
print('O_(")(")')
print('')
print('(\\(\\ \n( -.-) \nO_(")(")')
'''

1. Wejdź na stronę Wikipedii poświęconej Monty Pytonowi

        https://en.wikipedia.org/wiki/Monty_Python

Skopiuj fragment z paragrafu zatytuowanego "Monty Python".

2. W skrypcie utwórz zmienną article i przypisz jej wartość skopiowanego tesktu.

Uwaga! Skopiowany tekst jest długi i zawiera znaki ENTER. Jeśli chcesz przypisać do zmiennej taki tekst możesz użyć konstrukcji z trzema apostrofami o tak:

zmienna = '''
#dłuuugi tekst i jeszcze
#dłuższy tekst i....
'''

3. Skonwertuj tekst do dużych liter i wyświetl go. Zrób to w jednej instrukcji.

4. Wyświetl tekst zamieniając 'monty' na 'flying'. Ponieważ python rozpoznaje małe i duże litery przed zamianą skonwertuj go na małe litery. 
Ponownie postaraj się to zrobić w jednym poleceniu.

5. Rozbij tekst na słowa ze względu na spacje i wyświetl tą listę.

6. Wyświetl tekst w postaci:
        word python appears 3 times 
oczywiście liczba (tutaj 3) powinna być wyliczona, jako ilość wystąpień tekstu python w zmiennej article

7. Poleceniem print wyświetl tekst:
to print the \ you need to put \ twice in your text like this: \\ 

8. Poleceniem print wyświetl tekst

The best hits of '80s!!! 

Zrób to na 2 sposoby:
-raz tekst powinien być zamknięty w pojedynczym apostrofie '
-a drugi raz tekst powinien być zamknięty w cudzysłowiu "

9. Teraz zrobisz "mini kalkulator" do kantoru wymiany walut. Chcemy wyświetlić tabelkę w postaci:

cur   exchange amount
USD   3.65     64.10958904109589
EUR   4.23     55.31914893617021
w tym celu:

-najpierw zadeklaruj zmienną amountPLN i wpisz do niej wartość 234

-następnie wyświetl teksty rozdzielając wartości tabulatorem, tak aby to co zostanie wypisane na ekranie przypominało tabelkę (skorzystaj do tego z kilku poleceń print, jednolinijkowy print byłby zbyt trudny do zrozumienia)

-wartości w kolumnie amount wylicz dzieląc amountPLN przez aktualny kurs USD i EUR (w tym przykładzie są to 3.65 i 4.23)

10. Zadeklaruj zmienną ValueAsText i wpisz do niej wartość '123.45'

11. Zadeklaruj zmienną factor o wartości 1.23

12. Wyświetl tekst:

value is  123.45 factor is 1.23 value*factor= 151.8435 

podczas obliczania value * factor skonwertuj zmienną ValueAsText na typ float
'''

#stringi - podsumowanie
articel = '''
Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and impact, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]

Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, including Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.

At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution To Cinema. In 1998 they were awarded the AFI Star Award by the American Film Institute. Many sketches from their TV show and films are well-known and widely quoted. Both Holy Grail and Life of Brian are frequently ranked in lists of greatest comedy films. In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]
'''
print(articel.upper())
print(articel.lower().replace("monty","flying"))
print(articel.split(" "))
print("word python appears", articel.lower().find("python"),"times")

text1 = "The best hits of '80s!!!"
text2 = 'The best hits of \'80s!!!'
print(text1,"\n",text2)

ammountPln = 234
usd = 3.65
eur = 4.23
print("cur\texchange\tamount")
print("USD\t",usd,"\t",ammountPln/usd)
print("EUR\t",eur,"\t",ammountPln/eur)

valueAsText = '123.45'
factor = 1.23

print("value is", valueAsText,"factor is",factor,"value*factor=",float(valueAsText)*factor)

'''
1. Zadeklaruj zmienną helloMessage i wpisz do niej tekst:

"Hello %s!"

2. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa powitania: raz %s należy zamienić na Kate a raz na Chirs

3. Zmień zawartość zmiennej helloMessage na

"Hello {0:s}!"

4. Podobnie , jak w punkcie drugim wyświetl powitanie z Kate i Chis, ale tym razem skorzystaj z metody format

5. Zmień zawartość zmiennej helloMessage na

"%s has %d %s"

6. Korzystając z tej zmiennej oraz z operatora % wyświetl dwa komunikaty.

w pierwszym komunikacie %s zamień na Kate, %d na 1, a %s na animal

w drugim komunikacie %s zamień na  Chris, %d na 100000, a %s na $

7. Zmień zawartość zmiennej helloMessage na

"{0:s} has {1:d} {2:s}"

8. Wyświetl te same komunikaty, jak w punkcie 6, ale tym razem skorzystaj z metody format

9. [Trochę trudniejsze, ale cała trudność polega na samodzielnym zbudowaniu napisu formatującego i to w takiej postaci, 
że na każdy element w napisie ma zostać przewidziana określona liczba znaków]
Utwórz zmienną line i wpisz do niej tekst pozwalający na wyświetlenie na 20 znakach pewnego napisu, następnie słowa 
"costs", następnie na 6 znakach pewnej liczby i następnie znaku €, np:

ICE CREAM            costs      3 €
TRIP TO VENICE       costs    119 €
PIZZA HAWAII         costs      6 €
... BTW, wiesz jak uzyskać znak € z klawiatury? O ile używasz Windows powinien zadziałać prawy ALT + u

10. Korzystając ze zmiennej line i polecenia print,  zamieniaj odpowiednie znaczniki na podane niżej wartości, tak aby w efekcie został wyświetlony cennik usług:

ICE CREAM    3
TRIP TO VENICE  119
PIZZA HAWAI  6
'''

#formatowanie napisów
helloMessage = "Hello %s!"
print(helloMessage % "Kate")
print(helloMessage % "Kris")
helloMessage2 = "Hello {0:s}!"
print(helloMessage2.format("Kate"))
print(helloMessage2.format("Kris"))
helloMessage3 = "%s has %d %s"
print(helloMessage3 % ("Kate",1,"animal"))
print(helloMessage3 % ("Kris",100000,"$"))
helloMessage4 = "{0:s} has {1:d} {2:s}"
print(helloMessage4.format("Kate",1,"animal"))
print(helloMessage4.format("Kris",100000,"$"))

line1 = "%20s costs %6d"
print(line1 % ("ICE CREAM",3))
print(line1 % ("TRIP TO VENICE",119))
print(line1 % ("PIZZA HAWAI",6))

line2 = "{0:20s}costs{1:6d}€"
print(line2.format("ICE CREAM",3))
print(line2.format("TRIP TO VENICE",119))
print(line2.format("PIZZA HAWAI",6))


'''
1. Zadeklaruj zmienną name i przypisz do niej swoje imie

2. Zadeklaruj zmienną age i przypisz do niej wiek

3. Zadeklaruj zmienną daysInYear i przypisz jej wartość 365

4. Zadekraruj zmienną message i przypisz jej wartość jak poniżej. Uwaga w miejscu ??? należy umieścić znaczniki pozwalające na wyświetlenie kolejno napisu i dwóch liczb

'??? is ??? years old, so is about ??? days old' 

5. Wyświetl informację jak poniżej (wykorzystaj funkcje formatowania napisów)j:

Jan is 26 years old, so is about 9490 days old 

6. Zmień imie i wiek w zmiennych name i age i jeszcze raz wyświetl komunikat korzystając z tej samej instrukcj co poprzednio

7. Zmień wartość zmiennej message na:

message = '{???} is {???} years old, so is about {???} days old' 

Ponownie w miejscu ??? należy umieścić odpowiednie napisy formatujące pozwalające wyświetlić napis i 2 liczby

8. Stosując metodę format dla zmiennej message wyświetl komunikat w postaci:

Chris is 17 years old, so is about 6205 days old 

9. Wyznacz wynik dzielenia całkowitego i resztę z dzielenia 1234567890 przez 12345:

Wynik powinien wyglądać tak:

1234567890 divided by 12345 is  100005 and the rest is 6165 
'''

#typy numeryczne
name = "Michal"
age = 39
daysInYear = 365
message1 = '%s is %d years old, so is about %d days old'
print(message1 % (name,age,(age*daysInYear)))

message2 = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message2.format(name,age,(age*daysInYear)))

x = 1234567890
y = 12345
message3 = "{0:d} divided by {1:d} is {2:d} and the rest is {3:d}"
print(message3.format(x,y,(x//y),(x%y)))


'''
Zostajesz zatrudniony(a) do stworzenia oprogramowania pokładowego nowoczesnego samochodu. Aktualnie Twoim zadaniem jest oprogramowanie sterownika odpowiedzialnego za automatyczne włączanie świateł mijania w samochodzie. Będziesz pracować z następującymi zmiennymi:

isAutomaticMode - zmienna logiczna, o następującym znaczeniu: wartość True oznacza, że kierowca ustawił pokrętło sterujące światłem na tryb automatyczny. Sterownik ma podejmować decyzję o zapaleniu świateł tylko jeżeli wartość tej zmiennej to True, ale zapalenie świateł zależy jeszcze od kolejnych warunków,

is80PercentLight - zmienna logiczna o następującym znaczeniu: wartość True oznacza, że "chyba" mamy dzień, bo jest dość dużo światła. Światła w samochodzie powinny być zgaszone o ile nie ma innych warunków, które wpływałyby na to, że światła mają się świecić. Jeśli wartość zmiennej to False, tzn. że jest dość ciemno i światła powinny się zaświecić, oczywiście o ile jesteśmy w trybie automatycznym

isDirectLight - zmienna logiczna o następującym znaczeniu: wartość True oznacza, że nisko położone słońce świeci wprost w oczy kierowcy. Wprawdzie ciemno nie jest, ale w takich warunkach światła powinny się zaświecić, oczywiście jeśli jesteśmy w trybie automatycznym

isRainy - zmienna logiczna o następującym znaczeniu: wartość True oznacza, że pada deszcz, jest mgła lub mamy do czynienia z innymi niekorzystnymi warunkami atmosferycznymi. O ile jesteśmy w trybie automatycznym, to należy zaświecić światła

Do zmiennej turnLightsOn zapisz wynik wyrażenia, które w oparciu o w/w zmienne ustali, czy światła mają zostać zapalone czy nie. Potem wyświetl wynik korzystając z instrukcji:

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
Przetestuj działanie wyrażenia zmieniając początkowe wartości zmiennych wejściowych, np:

isAutomaticMode = True
# is the level of day-lighr above 80%
is80PercentLight = True
# is the Sun ligthing directly into the driver's face
isDirectLight = False
# is it rainy, foggy or other weather conditions are present
isRainy = False
>> światła powinny się NIE świecić

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False
>> światła powinny się świecić

isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True
>> światła powinny się świecić

isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRainy = False
>> światła powinny się świecić

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = True
>> światła powinny się świecić

isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True
>> światła powinny się NIE świecić
'''
isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRainy = True
turnLightsOn = isAutomaticMode and not(is80PercentLight or isDirectLight or isRainy)


print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)






