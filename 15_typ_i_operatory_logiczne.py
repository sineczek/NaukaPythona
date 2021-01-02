#
isWeekend = True
print("Is weekend =",isWeekend)

temp = 25
print("Temperature = ",temp)

toDoList = 'Shopping'
print("ToDoList =",toDoList)

isHappy = isWeekend and temp >= 20 and toDoList == ''
print("IsHappy =",isHappy)

isHappy = not isWeekend and temp < 20 and toDoList != ''
print("IsHappy =",isHappy)

#\ na końcu linijki dzieli kod i można kontynuować w następnej linii
isHappy = isWeekend and temp >= 20 and toDoList == '' \
or not (isWeekend and temp >= 20) and toDoList != ''
print("IsHappy =",isHappy)