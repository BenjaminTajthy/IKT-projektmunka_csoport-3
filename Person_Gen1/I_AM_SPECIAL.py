from time import sleep
from os import system

Spendable_pts = 10

Intelligence =  1
Charisma = 1
Luck = 1
Strength = 1
Agility = 1
Endurance = 1

pg1 = r'C:\Users\BeniTajthy\Documents\GitHub\IKT-projektmunka_csoport-3\IMSPECIALTXTS\Pg1.txt'
pg2 = r'C:\Users\BeniTajthy\Documents\GitHub\IKT-projektmunka_csoport-3\IMSPECIALTXTS\Pg2.txt'
pg3 = r'C:\Users\BeniTajthy\Documents\GitHub\IKT-projektmunka_csoport-3\IMSPECIALTXTS\Pg3.txt'
pg4 = r'C:\Users\BeniTajthy\Documents\GitHub\IKT-projektmunka_csoport-3\IMSPECIALTXTS\Pg4.txt'
pg5 = r'C:\Users\BeniTajthy\Documents\GitHub\IKT-projektmunka_csoport-3\IMSPECIALTXTS\Pg5.txt'
pg6 = r'C:\Users\BeniTajthy\Documents\GitHub\IKT-projektmunka_csoport-3\IMSPECIALTXTS\Pg6.txt'

pg1l = open(pg1, 'r').read(), Intelligence
pg2l = open(pg2, 'r').read(), Charisma
pg3l = open(pg3, 'r').read(), Luck
pg4l = open(pg4, 'r').read(), Strength
pg5l = open(pg5, 'r').read(), Agility
pg6l = open(pg6, 'r').read(), Endurance


book = [pg1l, pg2l, pg3l, pg4l, pg5l, pg6l]
booklen = len(book)

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

Book()
