persons=['Elizabeth','Steven','Sebastian','Margaret','Svetlana','Raphael']

domain = 'mycompany.com'

for person in persons:
    email = person.lower() + '@' + domain
    print('Email for\t', person, '\tis\t', email)
else:
    print('End of the list --')





