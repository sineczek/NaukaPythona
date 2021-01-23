from datetime import date
from datetime import timedelta
def GiveWorkingday(year=date.today().year, \
                   month=date.today().month, \
                   day=date.today().day):
    #print the nearest working day date


    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday #funkcja zwraca wyliczoną datę jako workingday

nextWorkingday = GiveWorkingday()
print('Next workingday after today is:', nextWorkingday)
nextWorkingday = GiveWorkingday(2021,1,2)
print('Next workingday after:',2021,1,2,'is:',nextWorkingday)

print('Next workingday after today is:',GiveWorkingday()) #funkcja w princie
