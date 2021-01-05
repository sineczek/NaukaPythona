'''Przygotowujesz się do analizy email-marketingu. Po każdym zadaniu poniżej wyświetl listę:

1. Utwórz listę o nazwie marketing z elementami:
-loyality program
-client promotion
-market research

2. Dodaj do listy element 'public relations'
3. Wyświetl pozycję numer 3
4. Wstaw na pozycję numer 2 element 'investor relations'
5. Chcesz jednak aby lista znajdowała się w zmiennej o nazwie emailMarketing. Skopiuj elementy z listy marketing do listy emailMarketing
6. Posortuj listę emailMarketing
7. Utwórz nową jednoelementową listę internalEmails. Jedyny element to 'internal communication'
8. Dodaj listę internalEmails do listy emailMarketing
9. Utwórz tuple, którego wartości pochodzą z listy emailMarketing. Podczas wyświetlania tuple zwróć uwagę na nawiasy, z jakich skorzystał Python'''

marketing = ["loyality program","client promotion","market research"]
marketing.append("public relations")
print(marketing[3])
marketing.insert(2,"investor relations")
print(marketing)
emailMarketing = marketing.copy()

emailMarketing.sort()
print(emailMarketing)
internalEmails = ["internal communication"]
print(internalEmails)

emailMarketing.extend(internalEmails)

print(emailMarketing)
emailTuple = tuple(emailMarketing)
print(emailTuple)




