import random
import names
from  datetime import date
from time import sleep
from os import system

Illegal = bool()

rdint = random.randint

class Person:

    def cal(self, bdate):
        today = date.today()
        self.age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
        return self.age

    def Gender(self):
        gender = ['Female', 'Male']
        self.g = rdint(0,1)
        if self.g == 0:
            self.Gender = gender[0]
        else:
            self.Gender = gender[1]
        print(self.Gender)

    def name(self):
        fname = names.get_last_name()
        print(fname)

        if self.Gender == 'Male':
            sname = names.get_first_name('male')        
        elif self.Gender == 'Female':
            sname = names.get_first_name('female')
        
        print(sname)
        fullname = sname, fname
        print(fullname)

    def age(self):
        byear = rdint(1940, 2005)
        bmonth = rdint(1, 12)
        bday = rdint(1, 31)

        if bmonth == 2:
            bday = rdint(1,28)

        elif byear % 2 == 0 and bmonth == 2:
            bday == rdint(1,29)
        
        Age = self.cal(date(byear,bmonth,bday))
        bdate = byear, bmonth, bday

        print(Age)
        print(bdate)

    def place_of_birth(self):
    
        Cb = ['Arizona', 'California', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Oregon', 'Utah', 'Washington', 'Wyoming', 'Illinois', 'Indiana','Iowa', 'Kansas','Michigan' 'Minnesota','Missouri', 'Nebraska', 'North Dakota', 'Ohio','South Dakota', 'Wisconsin','Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia', 'Connecticut', 'Maine','Massachusetts', 'New Hampshire', 'New Jersey', 'New York', 'Pensylvania', 'Vermont']
        Ws = [Cb[rdint(0, 10)]]    #11 állam
        Mws = [Cb[rdint(11, 21)]]  #12 állam
        Ss = [Cb[rdint(22, 37)]]   #16 állam
        Ns = [Cb[rdint(38,45)]]    #8 állam

        self.place_of_birth = rdint(0, 100)

        if self.place_of_birth <= 25:
            self.place_of_birth = Ws
            print(self.place_of_birth)

        elif self.place_of_birth >= 26 and self.place_of_birth <= 50:
            self.place_of_birth = Mws
            print(self.place_of_birth)

        elif self.place_of_birth >= 51 and self.place_of_birth <= 75:
            self.place_of_birth = Ss
            print(self.place_of_birth)

        else:
            self.place_of_birth = Ns
            print(self.place_of_birth) #
