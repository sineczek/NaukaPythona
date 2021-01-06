age = 27
isDrunk = False
isRestrictedArea = False

#nestedIF
if age < 18:
    print("za młody")
else:
    if isDrunk:
        print("za wesoły")
    else:
        if isRestrictedArea:
            print("zła lokalizacja")
        else:
            print("DRINK! DRINK! DRINK!")
print("----")

#lepsiejsza
if age < 18:
    print("za młody")
elif isDrunk:
    print("za wesoły")
elif isRestrictedArea:
    print("zła lokalizacja")
else:
    print("DRINK! DRINK! DRINK!")
print("----")


