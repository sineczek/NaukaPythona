import time

# sprawdzenie wersji pythona
import sys
print(sys.version)

# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))

print('Current time is ... unix epoch', time.time()) #liczy się od 1.1.1970, a liczy w sekundach
print('\n')
print('Current time is ... tuple',      time.localtime(time.time()))
print('\n')
print('Current time is ... for human',  time.asctime(time.localtime(time.time())))
print('\n')
#print('Current time is ... for human',  time.localtime(time.clock()))
print('\n\n\n')

import calendar
print('----------------------------------------')
print(calendar.month(2021,1,w=5,l=2)) #5 znaków na każdy dzieńm odstępy po 2 znaki
print('----------------------------------------')
print(calendar.month(2021,1)) #bez odstępów
print('----------------------------------------')
print('week day is', calendar.weekday(2021,1,18)) #weekday 0 czyli poniedziałek, bo liczymy od 0
print('----------------------------------------')
calendar.setfirstweekday(6) #jaki dzień jest pierwszy przy rysowaniu kalendarza (6 czyli niedziela)
print('----------------------------------------')
print(calendar.month(2021,1))
print('----------------------------------------')
print('week day is', calendar.weekday(2021,1,18))
print('----------------------------------------')
print('is 2021 a leap year?',calendar.isleap(2021)) #czy rok przestępny
print('----------------------------------------')
print('Leap days 2000-2017', calendar.leapdays(2000,2017)) #ile dni przestępnych
print('----------------------------------------')
print('Leap days 2000-2020', calendar.leapdays(2000,2020))
print('----------------------------------------')
print('Leap days 2000-2021', calendar.leapdays(2000,2021))
print('----------------------------------------')
print(calendar.calendar(2021)) #rysuje piękny kalendarz



