'''Tym razem pomożemy lekarzom przeprowadzając wstępną analizę:
czy pacjent ma grypę, czy tylko przeziębienie (zakładamy, że pacjentowi coś dolega, w tym zadaniu mamy tylko pomóc zdiagnozować
czy to jest grypa czy przeziębienie):

1, Utwórz 3 zmienne

-musclePain - wartość false
-fever - wartość true
-weakness - wartość true

2. Napisz wyrażenie if, które

-jeśli występują wszystkie 3 objawy wyświetli komunikat "suspicion of influenza"
-w przeciwnym razie wyświetli "The flu is unlikely"

3. Napisz wyrażenie if, które:

-jeśli występują wszystkie 3 objawy wyświetli komunikat "suspicion of influenza"
-jeśli występuje osłabienie (weakness) ale nie ma gorączki lub nie ma bólu mięśni to wyświetli "Just take a rest!"
-w przeciwnym razie wyświetli "you may be cold"

4. Mężczyźni przeziębienie przechodzą jak grypę... dodaj zmienną isMan o wartości true

5. Napisz wyrażenie if, które:

-komunikat o grypie wyświetli jeżeli występują wszystkie 3 objawy lub co najmniej jeden z nich o ile pacjent jest mężczyzną
-w pozostałych przypadkach zachowanie ma być jak w  poprzednim przykładzie

6. Zmieniamy temat. Pilot przed wystartowaniem powinien sprawdzić listę kontrolną. Właśnie piszesz kod,
który odpowiada za wyświetlenie napisu "CHECK IS COMPLETED" jeżeli lista kontrolna została już pomyślnie wykonana i zamknięta,
w przeciwnym razie powinien być wyświetlany komunikat "CHECK NOT DONE YET!". Zmienna True/False, która zawiera informację o tym
czy lista kontrolna została już wykonana nazywa się isCheckCompleted. Korzystając z ternary operator przygotuj polecenie if wyświetlające odpowiedni komunikat'''

isMan = False
musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print("suspicion of influenza")
else:
    print("The flu is unlikely! You are fine! ;)")
print("---------")

if weakness and musclePain and fever:
    print("suspicion of influenza")
elif musclePain or weakness and not fever:
    print("Just take a rest!")
elif (weakness and fever and not musclePain) or (musclePain and fever and not weakness):
    print("you may be cold")
else:
    print("The flu is unlikely! You are OK!")
print("---------")

if isMan and weakness or fever or musclePain:
    print("suspicion of influenza")
elif not isMan and weakness and musclePain and fever:
    print("suspicion of influenza")
elif not isMan and musclePain or weakness and not fever:
    print("Just take a rest!")
elif not isMan and (weakness and fever and not musclePain) or (musclePain and fever and not weakness):
    print("you may be cold")
else:
    print("The flu is unlikely! You are OK!")
print("---------")
if musclePain and fever and weakness or  isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("this only cold")
print("---------")
isCheckCompleted = False

print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")