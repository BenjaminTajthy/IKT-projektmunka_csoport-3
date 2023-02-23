class StartMenu:
    print('      Name      ')
    print('1. Start')

class PAccount:
    StartMenu()
    uinput = input('Type: ')
    if int(uinput) == 1:
        print('What is your name?')
        uinput = input('Type: ')
        pname = str(uinput)
        print('Hello', pname)
    
    print('1. ')
    print('2. ')
    print('3. ')
    print('4. ')
    print('5. ')

PAccount()