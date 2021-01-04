'''
    Czy wiesz, że twórca języka Python - Guido Van Rossum - był fanem latającego cyrku Monty Pythona? Tak. To od tego wzięła się nazwa języka!

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

#2.
articel = '''
Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and impact, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "an important moment in the evolution of television comedy".[7]

Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, including Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.

At the 41st British Academy Film Awards in 1988, Monty Python received the BAFTA Award for Outstanding British Contribution To Cinema. In 1998 they were awarded the AFI Star Award by the American Film Institute. Many sketches from their TV show and films are well-known and widely quoted. Both Holy Grail and Life of Brian are frequently ranked in lists of greatest comedy films. In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]
'''

#3.
print(articel.upper())

#4.
print(articel.lower().replace("monty", "flying"))

#5.
print(articel.split(' '))

#6.
print("word python appears", articel.lower().count('python'), "times")

#7.
print(r"to print the \ you need to put \ twice in your text like this: \\")

#8.
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")

#9.
amountPLN=234
print('cur','\texchange','amount')
print('USD',"\t",3.65,"\t",amountPLN/3.65)
print('EUR','\t',4.23,"\t",amountPLN/4.23)

print('cur   exchange amount \nUSD   ', 3.65, '   ', amountPLN/3.65, '\nEUR   ', 4.23, '   ', amountPLN / 4.23)

#10.
valueAsText = '123.45'
print(valueAsText)

#11.
factor =1.23
print(factor)

#12.
print('value is', valueAsText,'factor is',factor,'value*factor=',float(valueAsText)*factor)





