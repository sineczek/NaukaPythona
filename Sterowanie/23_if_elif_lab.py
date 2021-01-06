'''1. Jak pamiętasz (mam nadzieję) sklep odzieżowy uruchamiał promocję tylko jeżeli ilość lajków była większa lub równa 500
a ilość udostępnień co najmniej 100. Kiedy oba warunki były spełnione sprawa była prosta - rozpoczynała się obniżka cen.
Kiedy jednak brakowało lajków lub udostępnień, to wypadałoby dać znać czego brak.

Najpierw napisz zagnieżdżone wyrażenie if / else, a potem przekształć do postaci if/elif/else. Możesz to zrobić "po swojemu",
ale jak chcesz możesz stosować się do moich podpowiedzi. To propozycje kroków w rozwiązaniu z zagnieżdżonymi if/else

jeśli warunki są spełnione - świetnie, rozpoczynamy promocj

w przeciwnym razie

jeśli brakuje lajków wyświetl informację o braku lakjów

w przeciwnym razie (musi brakować udostępnień - to logiczne!)

wyświetl informację o braku udostępnień

Przepisujac instrukcje do if/elif/else stosuj sie do tych zaleceń:

jeśli warunki są spełnione, zaczynamy promocję

w przeciwnym razie jeśli ilość lajków jest za mała - wyświetl komunikat o brakujących lajkach

w przeciwnym razie wyświetl komunikat o brakujących udostępnieniach'''

minLikes = 500
minShares = 100
numLikes = 1130
numShares = 500

if numLikes <= minLikes:
    print("We still need more likes to start the promotion.")
else:
    if numShares <= minShares:
        print("'We still need more shares to start the promotion.")
    else:
        print("All prizes drop 10%!!")
print("-----")
if numLikes <= minLikes:
    print("We still need more likes to start the promotion.")
elif numShares <= minShares:
    print("'We still need more shares to start the promotion.")
else:
    print("All prizes drop 10%!!")
print("----------------")

'''2. Restauracja oferowała kupon na burgera, jeżeli zamówiłeś pizzę lub duży napój w dzień nie będący dniem weekendowym. 
Kiedy warunki promocji były spełnione, sprawa była prosta - dajemy kupon. Jednak w przypadku niespełnienia warunków wypadałoby poinformować, 
który warunek nie jest spełniony.

Wskazówki do rozwiązania z zagnieżdżonym if/else

jeżeli warunki są spełnione wydajemy kupon na burgera

w przeciwnym razie

jeżeli jest weekend, to wyświetlamy informację, że promocja dotyczy tylko dni poza weekendem

w przeciwnym razie (już wiadomo, że to nie jest weekend, więc brakło na zamówieniu pizzy lub dużego napoju!)

wyświetlamy informację o braku pizzy

Przepisując rozwiązanie na if/elif/else stosuj się do wskazówek:

jeśli warunki są spełnione - wydaj kupon na burgera

w przeciwnym razie jeśli jest to weekend, wyświetl komunikat o tym, że promocja obowiązuje wyłącznie w poza weekendem

w przeciwnym razie wyświetl komunikat o tym, że należy zamówić pizze lub duży napój



Pamiętaj, że stosowanie if/elif/else jest znacznie lepsze jeśli chodzi o styl programowania!'''

isWeekend = True
isPizzaOrdered = True
isBigDrinkOrdered = True

if isWeekend:
    print("Only on weekdays")
else:
    if not isPizzaOrdered:
        print("Buy Pizza to get free Burger coupon!")
    else:
        if isBigDrinkOrdered:
            print("Buy Big Soda to get free Burger coupon!")
        else:
            print("You get free Burger coupon!")
print("----")
if isWeekend:
    print("Only on weekdays")
elif isPizzaOrdered:
    print("Buy Pizza to get free Burger coupon!")
elif isBigDrinkOrdered:
    print("Buy Big Soda to get free Burger coupon!")
else:
    print("You get free Burger coupon!")
print("--------------------")

