#słowniki
countryLeaders={'PL':'Dupa','US':'Trump'}

print(countryLeaders)

print(countryLeaders['US'])

countryLeaders['DE'] = "Merkel" #dodawanie nowej pozycji w słowniku
print(countryLeaders)

#print(countryLeaders.values()) #wyświetla wartości
#print(countryLeaders.items()) #kolekcja elementów
#print(countryLeaders.keys()) #wyświetla klucze

print(countryLeaders.popitem()) #destruktywna iteracja po słowniku

print(countryLeaders.setdefault('FR','Macron')) #prosimy o wyświetlenie, jeśli nie ma podajemy kolekcję, ktora zostaje na stałe dodana
print(countryLeaders.get("RU")) #nie dodaje nowego tylko sprawdza czy coś jest

newLeaders = {"RU":"Putin","US":"Biden"}
print(newLeaders)
countryLeaders.update(newLeaders) #przekazywanie nowej listy, a jak klucz się powtarza to go nadpisze
print(countryLeaders)



