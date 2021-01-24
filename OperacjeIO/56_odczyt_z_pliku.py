'''file = open('c:\\temp\\plik.txt','r')

content = file.read()
print(content)

file.close() #zawsze należy pamiętać przy takiej metodzie o zamknięciu pliku



#lepiej, ale przy dużych plikach niewydajne
with open('c:\\temp\\plik.txt','r') as file:
    content = file.read()
    print(content)
'''


#linijka po linijce - najlepsze do dużych plików
with open('c:\\temp\\plik.txt','r') as file:
    for line in file:
        print(line)

#ilość bajtów
file = open('c:\\temp\\plik.txt','r')

fragment = file.read(10) #czytaj po 10 bajtów
while fragment:
    print(file.tell(),fragment) #file.tell() wskazuje ile przeczytaliśmy
    fragment = file.read(10)
file.close()
