from datetime import date
from datetime import timedelta
def GiveWorkingday(year=date.today().year,\
                   month=date.today().month,\
                   day=date.today().day): #domyślny parametr day=1
    #print the nearest working day date


    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for', day, 'is', workingday)
    return

GiveWorkingday()
GiveWorkingday(2021,1,2)
GiveWorkingday(2021,2) #ale wywłanie np. 31.01 spowoduje sprawdzenie daty dla 31 lutego!!
