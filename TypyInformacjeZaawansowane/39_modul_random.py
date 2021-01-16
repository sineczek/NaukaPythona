import random
print('One random number:', random.randint(1,100)) #1 <= N <=100
print('------------------------------------------------\n')

print('Choosing random number from a range:', random.choice((range(1,100)))) #
print('------------------------------------------------\n')

print('Choosing random number from range - easier:', random.randrange(1,100)) #robi to samo co poprzednie, ale łatwiejszy zapis
print('------------------------------------------------\n')

list=['John','Ann','Peter','Susan','Emily','Greg','Chris']
random.shuffle(list)
print('Recorded list:', list)
print('------------------------------------------------\n')

print("Just a random float:", random.random()) #float z zakresu 0 - 1
print('------------------------------------------------\n')


