class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print('Vehicle make=', self.make, 'model=', self.model, "year=", self.year)

class Car(Vehicle):
    def start_engine(self):
        print('Car make=', self.make, 'model=', self.model, "year=", self.year)

class Motorcycle(Vehicle):
    def start_engine(self):
        print('Motor Cycle make=', self.make, 'model=', self.model, "year=", self.year)