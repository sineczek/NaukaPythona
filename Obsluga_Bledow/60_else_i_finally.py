import sys
taskPerPerson = 0

try:
    tasks = 32

    personStr = input('How many persons ore there in the team? ')
    persons = int(personStr)

    taskPerPerson = tasks / persons

except ValueError as e: #dzięki dodaniu do zmiennej można np. zapisać error do loga
    print('Sorry - You need to enter intiger number: ', e)

except ZeroDivisionError as e:
    print('Sorry - You need to enter value > 0: ',e)

except:
    print('Something went wrong ....',sys.exc_info()[0])

else: #jeśli nie było błedu/wyjątku w try:
    print('Every person shoul have around', taskPerPerson, 'tasks')

finally: #to co tu będzie zawsze się wyświetli, nie wazne czy był wyjątek czy też nie
    print('Script finished with/without errors') #świetne miejsce na zamykanie plików jeśli otwieraliśmy jakieś
    #może posłużyć do tzw. cleanUpu


