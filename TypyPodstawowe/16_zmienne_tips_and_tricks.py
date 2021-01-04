title = "Python"
print("Title is", type(title))

version = 3
print("Version is", type(version))

progress = 0.21
print("Progress is", type(progress))

print("The expression is", type(progress*version))

x=1
y=1
z=1
print(x,y,z)
#lepiej można zrobić to - inicjowanie zmiennych
a=b=c=2
print(a,b,c)
c=3
print(a,b,c)

#kolejność działań jak w matematyce
print(2+2*2)
print(6/2*(1+2)) #wynik jest float

print(4**3**2) #potęgowanie

x=1
x+1
print(x) # x =1 nadal, bo nie zmieniliśmy zmiennej

x=x+1
print(x) # teraz x = 2

x+=1 #szybszy zapis x=x+1
print(x) #teraz to 3

'''
x++ # w pythonie to nie działa
print(x)
'''






