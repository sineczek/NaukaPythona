#czyli dodawanie napisów

drive = "c:\\" #bo \ ma różne znaczenia dla następnego znaku
folder = "scripts\\python\\"
file = "myscript.py"

path = drive + folder + file

print(path) # ładnie interpretuje
path #nieinterpretetuje - będą \\

justText = "text \nnewline" #\n zostanie przyjęte jako znak nowej linii
print(justText)
justText2 = r"text \nnewline" #r oznacza surowy text i niejest interpretowane np. \n
print(justText2)

# możn stosować albo "" albo ''

justText3 = "Mc Donald's" #będzie działać
#justText4 = 'Mc Donald's' nie będzie działać bo ' używa jako końca i początku textu

print(justText3)
#print(justText4)






