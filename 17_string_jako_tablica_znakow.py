s="A Python script"
print(s[0])
print(s[2])

#parsowanie tekstu
#odwoływanie się do liter w napisie, w tablicy, robimy za pomocą []

print(s[2:7]) #7 znak nie jest brany pod uwagę

print(s[2:8])

print(s[:8]) #wszystkie znaki do 8
print(s[8:]) #wszystkie znaki od 8 do końca

print(s[2:999]) #nie ma problemu, że jest mniej znaków
print(s[222:999]) #też nie ma problemu, nic tam nie ma wieć zbiór pusty

message = 'Document "cv.doc" was printed on printer: XEROX'
#nazwa drukarki
print(message.find(':'))
print(message[message.find(':'):]) #tu zwróci : XEROX
print(message[message.find(':')+2:]) # tu już samo XEROX

#nazwa dokumentu
print(message[message.find('"')+1:])  #tu od pierwszego " do końca wyrażenia
tmp = message[message.find('"')+1:] #teraz w zmiennej tmp mamy tą część
print(tmp[:tmp.find('"')]) #ze zmiennej tmp bierzemy wszytsko aż do " i dizeki temu mamy nazwę dokumentu





