cargo=[40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()
print("The cargo list:", cargo)
boxCapacity = 90
box = []
i=0

while i<len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box) >= cargo[i]):
        box.append(cargo[i])
    i+=1

print("The collected items sum is:",sum(box))
print("The elemnts are", box)

print("---------------------------------------------------")