
#1. Zadeklaruj zmienną name i przypisz do niej swoje imie
imie = 'Michal'
#2. Zadeklaruj zmienną age i przypisz do niej wiek
age=39
#3. Zadeklaruj zmienną daysInYear i przypisz jej wartość 365
daysInYear = 365
'''4. Zadekraruj zmienną message i przypisz jej wartość jak poniżej. Uwaga w miejscu ??? należy umieścić znaczniki pozwalające na wyświetlenie kolejno napisu i dwóch liczb

'??? is ??? years old, so is about ??? days old' 
'''
message1='%s in %d years old, so is about %d days old'

'''5. Wyświetl informację jak poniżej (wykorzystaj funkcje formatowania napisów)j:

Jan is 26 years old, so is about 9490 days old 
'''
print(message1 % (imie, age, (age*365)))

#6. Zmień imie i wiek w zmiennych name i age i jeszcze raz wyświetl komunikat korzystając z tej samej instrukcj co poprzednio



'''7. Zmień wartość zmiennej message na:

message = '{???} is {???} years old, so is about {???} days old' 

Ponownie w miejscu ??? należy umieścić odpowiednie napisy formatujące pozwalające wyświetlić napis i 2 liczby
'''
message2='{0:s} in {1:d} years old, so is about {2:d} days old'
print(message2.format(imie, age, (age*365)))
'''8. Stosując metodę format dla zmiennej message wyświetl komunikat w postaci:

Chris is 17 years old, so is about 6205 days old 
'''
print(message2.format(imie, age, (age*365)))
'''9. Wyznacz wynik dzielenia całkowitego i resztę z dzielenia 1234567890 przez 12345:

Wynik powinien wyglądać tak:

1234567890 divided by 12345 is  100005 and the rest is 6165

'''

x = 1234567890
y = 12345
message3 = "{0:d} divided by {1:d} is {2:d} and the rest is {3:d}"
print(message3.format(x, y, (x//y), (x % y)))

happy = "Happy"
new = "New"
year = "Year"
year1 = 2021

message = "{0:5s} {1:3s} {2:4s}! {3:4d} !"
print(message.format(happy,new,year,year1))