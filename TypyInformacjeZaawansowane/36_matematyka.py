f_smaller = 3.141592653589279
f_bigger = 3.87756392769

print(f_smaller, f_bigger)
print('\n')

print(int(f_smaller), int(f_bigger)) #rzutowanie na typ int czyli bez tego co po przeciny
print('\n')

print(abs(f_smaller), abs(-f_bigger)) #wartość bezwzględna (absolutna)
print('\n')

print(round(f_smaller,2), round(f_bigger,2), round(f_bigger,3)) #zaokrąglanie, 5 zaokrąglane w górę zgodnie z regułami matematyki
print('\n')

print(min(f_smaller,f_bigger), max(f_smaller,f_bigger)) #wartość namniejsza i największa
print('\n')

list=[1,2,3,4,5,4,4,5,4]

print(sum(list), len(list))
print('\n')

print(sum(list)/len(list)) #wyliczenie średniej bez importowani a modułu
print('\n')

print(round(2.675, 2)) #tu specyfika float - nie jest precyzyjny.. powinno być 2.68
