8*4

five = 5
three = 3
print(five*three)

print(type(five))

print(type(five*three))

#int opisuje liczby całkowite, nieważne czy ujemne czy dodatnie

print(five/three)
print(type(five/three))

#float liczby niecalkowite, jednak zaokrągla, więc nie jest dokładny

import sys
print(sys.maxsize)

veryBigValue = 99999999999999999999999999999999999999999
print (veryBigValue)
print(veryBigValue+1)
print(type(veryBigValue))
print(veryBigValue+1/2) #niby całkowita, ale jest przez pythona jako float
print(type(veryBigValue+1/2))
print(five//three) #// oznacza dzielenie całkowite
#dzielenie modulo - kiedy chcemy wiedzieć ile wynosi reszta z dzielenia
print(five % three)

print(float('inf')) #rzutowanie, próbuje zamienić na liczbę napis
#tak tworzy się "nieskończoność"

print(float('inf')>999999999999999999999999999999999999999999999999999)
print(-float('inf')) # -nieskończoność





