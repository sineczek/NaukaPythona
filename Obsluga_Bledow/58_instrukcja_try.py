taskPerPerson = 0

tasks = 32

personStr = input('How many persons ore there in the team? ')
persons = int(personStr)

taskPerPerson = tasks / persons

print('Every person shoul have around', taskPerPerson, 'tasks')

#powyższe zadziała dobrze jak się poda cyfrę
#jak się poda str to będzie error: ValueError: invalid literal for int() with base 10: 'one'


#opcja z try
#przy 0 też zwróci odpowiedniainformację
import sys
taskPerPerson = 0

try:
    tasks = 32

    personStr = input('How many persons ore there in the team? ')
    persons = int(personStr)

    taskPerPerson = tasks / persons
except:
    print('Something went wrong ....',sys.exc_info()[0]) #zwróci przy okazji informację jaki błąd

print('Every person shoul have around', taskPerPerson, 'tasks')











