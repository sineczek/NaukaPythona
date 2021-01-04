countries = ['FR','USA','DE','RU']
countries[1] = 'GB' #podmienianie
print(countries[1]) #odwołanie do miejsca na liście
countries.append('PL') #dodawanie na koniec
countries.insert(2, 'ES') #konkretne miejsce, reszta przesunięta
countries.remove('RU') #usówanie wpisu
countries.sort() #posortowało
countries.reverse() #odwrócona kolejność
print(countries.pop(2)) #zwraca wartość z pozycji a następnie ją wykasuje
print(countries.index('PL')) #czy występuje i na jakiej pozycji, ale jak brak na liście to dostanie się błąd
print(countries.count('DE')) #podaje ilość wystąpień


newList = ['FI','SE']
countries.extend(newList) #rozszerzanie listy o kolejną listę

countriesCopy = countries #można przypisać listę do nowej listy, ale to ta sama list, czyli jakby dodatkowa nazwa tylko
countriesCopy = countries.copy() #to na prawdę kopiuję listę
countriesCopy.clear() #czyści listę


print(countries)
print(countriesCopy)








