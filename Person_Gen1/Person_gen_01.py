import random
import names
from  datetime import date

rdint = random.randint

def cal(bdate):
    today = date.today()
    age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
    return age

class Person():

    def name():
    
        g = rdint(0,1)
        Gender = ['Female', 'Male']
        if g == 0:
            Gender = Gender[0]
        else:
            Gender = Gender[1]

        fname = names.get_first_name(Gender)
        sname = names.get_last_name()
        fullName = sname, fname
        print(Gender)
        print(fullName)
        print(fname)
        print(sname)


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

    name()
    age()
    place_of_birth()

Person()