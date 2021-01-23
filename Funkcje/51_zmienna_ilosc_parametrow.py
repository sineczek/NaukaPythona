def DoAction(action, parameter):
    print('action:',action)
    print('parameter:',parameter)
    return

DoAction('buy','shoes')
#DoAction('buy','shoes','socks') #za dużo


def DoAction2(action, *parameter): #gwiazdka oznacza kolecję parametrów
    print('action:',action)
    print('parameter:',parameter)
    for element in parameter:
        print("element is:", element)
    return

DoAction2('buy','socks','shoes','t-shirt')

def DoAction3(action, what, **parameter): #**zmienna staje się słownikiem
    print('action:',action)
    print('what:',what)
    print('parameter:',parameter)
    for element in parameter:
        print(element,'=',parameter[element])
    return
DoAction3('buy','shoes',size=45,color='brown',type='sport')


