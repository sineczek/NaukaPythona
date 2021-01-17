#drukowanie tabeli ASCI w zakresie od 32 (spacja) do 126 (~)
#for i in range(32,127):
#    print(i, chr(i))

ints = range(33,127) #bez spacji
password=''
import random
for i in range(16): #haslo 16 znakowe
    password+=chr(random.choice(ints))

print('New password is:', password)










