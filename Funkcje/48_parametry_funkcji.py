def GiveWorkingday(year, month, day): #takie zmienne będzie przyjmować funkcja
    #print the nearest working day date
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for', day, 'is', workingday)
    return

GiveWorkingday(2021,1,23) #ważna jest kolejność! - przekazanie przez kolejność
GiveWorkingday(year=2021,month=12,day=6) #jawne przekazanie nazwy przez funkcję - i można zmieniać kolejność
GiveWorkingday(day=6,year=2022,month=12)

