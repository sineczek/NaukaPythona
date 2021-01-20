width = 100
height = 20
numbers = [1]

line = ''               #to powinno być w funkcji
for n in numbers:
    line+= "%3d " % (n)

print(line.center(width))

for i in range (height-1):
    newNumbers = [1]
    position = 0
    while position < len(numbers) - 1:
        newNumbers.append(numbers[position] + numbers[position+1])
        position+=1
    newNumbers.append(1)
    numbers = newNumbers.copy()

    line = ''
    for n in numbers:
        line+= "%3d " % (n)
    print(line.center(width))





