#continue robi przeskok na początek pętli
persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@my.company.eu','Raphael']

domain = 'mycompany.com'

emails = []

for person in persons:

    if '@' in person:
        emails.append(person)
    else:
        email = person+'@'+domain
        emails.append(email)

for email in emails:
    print(email.lower())

print('------------------------')

persons=['Elizabeth','Steven@sales.mycompany.com','Sebastian','Margaret','Svetlana@my.company.eu','Raphael']

domain = 'mycompany.com'

emails = []

for person in persons:
    if '@' in person:
        emails.append(person)
        continue
    email = person+'@'+domain
    emails.append(email)

for email in emails:
    print(email.lower())

#jak jest continue nie musi być else




