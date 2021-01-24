filename = 'c:\\temp\\output.txt'

line = 'Europe'

cities = ['London','Berlin','Paris','Warsaw','Madrid','Rome']

file = open(filename,'a+')
# "w" czyli zapis, ale czyści zawartość,
# "a" dodaje do pliku - append
# "w+" do odczytu i zapisu równocześnie, ale czyści
# "a+" do odczytu i zapisu równocześnie, ale nie czyści

file.write(line) #pojedyncza linia
file.write('\n\n')
#file.writelines(cities) #dodanie listy

for city in cities:
    file.write(city+'\n')

file.close()





