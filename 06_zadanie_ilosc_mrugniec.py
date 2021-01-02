'''
    Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
    Zakladamy ze:
    -liczba mrugniec na minute to 20
    -liczba minut w godzinie to 60
    -liczba godzin w dobie 24
    -liczba lat (czyli nasz X) 50
    Uwaga: jezeli przyjac ze spimy 8 godzin to liczba godzin na dobe
    powinna wynosic 16


'''

#liczba mrugnięć okiem na minutę
blinksPerMin = 20

#liczba minut na godzinę i liczba godzin w dobie
minInHour = 60
hoursInDay = 24
daysInYear = 365

#liczba lat
years = 50

print(blinksPerMin * minInHour * hoursInDay * daysInYear * years)
