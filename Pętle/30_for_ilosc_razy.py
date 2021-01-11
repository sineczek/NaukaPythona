for number in range(20): #pozwala wygenerować zbiór liczb od 0 do określonej
    print(number)

for number in range(1,21): #można zakres wybrać
    print(number)

for number in range(1,21,2): #można określić skok
    print(number)

#czy liczba jest parzysta czy też nie
for number in range(1,21):
    if number %2 == 0:
        print("Number %2d is %s" % (number, 'even'))
    else:
        print("Number %2d is %s" % (number, 'odd'))





