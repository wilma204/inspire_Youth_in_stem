class car:
    def __init__(self,model,make,year_of_man,engine_capacity):
         self.model = model
         self.make = make
         self.year_of_man = year_of_man
         self.engine_capacity =engine_capacity


def get_model(self):
        return self.model

def get_model(self):
        return self.make

def get_model(self):
        return self.year_of_man

def get_model(self):
        return self.engine_capacity


#setters
def set_model(self,madel):
        return self.model

def set_model(self):
        return self.make

def set_model(self):
        return self.year_of_man

def set_model(self):
        return self.engine_capacity

#objects : instance of te classs
car1 = car("demio","nissan",2022,1300)
car2 = car("hilux","toyota",2022,3000)
car3 = car("passat","vw",2022,4000)


print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car2.get_year())

print(car3.get_model())
print(car3.get_year())