#starsza metoda

message1 = "Processing file %s"#%s nakazuje zintermretować literały jako resztę wiadomości
print(message1 % ("file_1.txt")) #i dzięki temu %s dodaje to co po %

message2 = "File %s has size %d KB" #%d jest do zastąpienia przez digit'a
print(message2 % ("file_1.txt", 100))

message3 = "File %20s has size %10d KB" #cyfra po % informuje ile znaków ma być zarezerwowanych dla zmiennych
print(message3 % ("file_1.txt", 100)) #to spowoduje pozostawienie pustego miejsca w komunikacie

#nowsza metoda
message4 = "Processing file {0:s}" #spodziewamy się jednego parametru string, 0 bo Python od 0 numeruje
print(message4.format("file1.txt")) #wywołaliśmy jedną metodę

message5 = "File {0:s} has size {1:d} KB"
print(message5.format("file1.txt", 100))

message5 = "File {1:s} has size {0:d} KB"
print(message5.format(100, "file1.txt")) #tu można zmieniać kolejność

message6 = "File {0:20s} has size {1:10d} KB" #można też przekazywać info o długości maksymalnej i rezerwować miejsce
print(message6.format("file1.txt", 100)) #tylko tu od początku wyświetla, a zarezerwowane są na końcu



