from os import system

def Book():
    currentpage = 0
    while True:
        uinput = input('Type: ')

        if uinput == 'next' and currentpage == booklen:
            system('cls')
            print("'", book[currentpage - 1], "'", currentpage, '/', booklen)

        elif uinput == 'next':
            currentpage = currentpage + 1
            system('cls')
            print("'", book[currentpage - 1], "'", currentpage, '/', booklen)

        elif uinput == 'back' and currentpage == 1:
            currentpage = currentpage + 1
            system('cls')
            print("'", book[currentpage - 2], "'", currentpage - 1, '/', booklen)

        elif uinput == 'back':
            currentpage = currentpage - 1
            system('cls')
            print("'", book[currentpage - 1], "'", currentpage, '/', booklen)

        elif uinput == 'stop':
            system('cls')
            break

        else:
            system('cls')
            print("Please write something that makes sense.")

