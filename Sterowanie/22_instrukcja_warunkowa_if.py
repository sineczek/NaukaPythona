age = 27

if age >= 18:
    print("You are adult and You can buy alcohol.") #musi być wcięcie
else:
    print("You are too young to buy alcohol")

isDrunk = False

if age >= 18 and not isDrunk:
    print("You are adult and You can buy alcohol.") #musi być wcięcie
else:
    print("We can't sell You alcohol")

isRestrictedArea = False

if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult and You can buy alcohol.") #musi być wcięcie
else:
    print("We can't sell You alcohol")




