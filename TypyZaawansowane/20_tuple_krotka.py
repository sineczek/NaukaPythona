#statyczne listy czyli krotka

tax = (4, 7, 8, 23) #przy tuple używamy ()

print(tax[2]) #odwołuje się tak samo
print(tax[-1]) #ostatni element
print(tax.index(7)) #odpowie na ktorym miejscu znajduje się '7'
print(tax.count(8)) #ilość wystąpień liczby '8'
print(max(tax)) #jaka wartość jest najwyższa,
# czyli można łączyć z innymi funkcjami pythona
print(tax)
'''
nie można (będzie błąd):
    -insert
    -append
    -revert
    -sort
    
czyli nie da się wpływać na listę
ale można skonwertować na listę
'''
taxList = list(tax)
taxList.append(30)
print(tax)
print(taxList)

newTax = tuple(taxList) #zmiana listy na tuple
print(newTax)

#wartości z tuple można szybko przyporządkować do zmiennych
(tax1,tax2,tax3,tax4) = tax
print(tax1,tax2,tax3,tax4)

a=1
b=10
print("a=",a,"\tb=",b)
#i teraz aby zamienić a i b trzeba stworzyć dodatkową zmienną np. temp
#temp = a
#a=b
#b=temp
(a,b)=(b,a) #tuple python może zmieniać w locie
print("a=",a,"\tb=",b)




