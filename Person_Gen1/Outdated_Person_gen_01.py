import random
import names
from  datetime import date
from time import sleep
from os import system

Illegal = bool()

rdint = random.randint

def cal(bdate):
    today = date.today()
    age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
    return age

def name():
    gender = ['Female', 'Male']
    g = rdint(0,1)
    if g == 0:
        Gender = gender[0]
    else:
        Gender = gender[1]
    print(Gender)

    if Gender == 'Male':
        sname = names.get_first_name('male')   
        print(sname)     
    elif Gender == 'Female':
        sname = names.get_first_name('female')
        print(sname)
    lname = names.get_last_name()
    print(lname)
    
def age():
    byear = rdint(1940, 2005)
    bmonth = rdint(1, 12)
    bday = rdint(1, 31)

    if bmonth == 2:
        bday = rdint(1,28)

    elif byear % 2 == 0 and bmonth == 2:
        bday == rdint(1,29)
    
    Age = cal(date(byear,bmonth,bday))
    bdate = byear, bmonth, bday

    print(Age)
    print(bdate)

def place_of_birth():

    Cb = ['Arizona', 'California', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Oregon', 'Utah', 'Washington', 'Wyoming', 'Illinois', 'Indiana','Iowa', 'Kansas','Michigan' 'Minnesota','Missouri', 'Nebraska', 'North Dakota', 'Ohio','South Dakota', 'Wisconsin','Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia', 'Connecticut', 'Maine','Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pensylvania', 'Vermont']
    Ws = [Cb[rdint(0, 10)]]    #11 állam
    Mws = [Cb[rdint(11, 21)]]  #12 állam
    Ss = [Cb[rdint(22, 37)]]   #16 állam
    Ns = [Cb[rdint(38,45)]]    #8 állam

    place_of_birth = rdint(0, 100)

    if place_of_birth <= 25:
        place_of_birth = Ws
        print(place_of_birth)

    elif place_of_birth >= 26 and place_of_birth <= 50:
        place_of_birth = Mws
        print(place_of_birth)

    elif place_of_birth >= 51 and place_of_birth <= 75:
        place_of_birth = Ss
        print(place_of_birth)

    else:
        place_of_birth = Ns
        print(place_of_birth)

def invsys():
    r = rdint(0,100)
    drugs = ["drug_x", "drug_y", "drug_z"]
    weapons = ["gun_a", "gun_b", "gun_c"]
    average = ["av_v", "av_d", "av_n"]

    illegal = []
    illegal.append(drugs[rdint(0,2)])
    illegal.append( weapons[rdint(0,2)])

    npcinventory = []

    if r <= 65:
        Illegal == True
        npcinventory.append(average[rdint(0,2)])
        npcinventory.append(illegal)
    else:
        for x in range(2):
            npcinventory.append(average[rdint(0,2)])
        Illegal == False
