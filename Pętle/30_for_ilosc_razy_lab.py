'''Dane są następujące napisy:

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
Korzystając z polecenia FOR wyświetl:

+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
Korzystając z polecenia FOR wyświetl:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Korzystając z polecenia FOR wyświetl:

x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx
(wskazówka: aby wyświetli 5 liter x użyj "x" *5



Korzystając z polecenia FOR wyświetl:

o
xx
ooo
xxxx
ooooo
xxxxxx
ooooooo
xxxxxxxx
ooooooooo'''

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for i in range(10):
    print(string_A)

for i in range(9):
    if i %2 == 0:
        print(string_A)
    else:
        print(string_B)

for i in range(10):
    print(i*"x")

for i in range(9):
    if i %2 == 0:
        print(i*'x')
    else:
        print(i*'o')
