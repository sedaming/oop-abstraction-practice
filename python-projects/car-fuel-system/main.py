
from abc import ABC, abstractmethod

class Car (ABC):

    @abstractmethod
    def show_speed (self):
        pass

    @abstractmethod
    def change_speed (self, speed):
        pass
    @abstractmethod
    def load_fuel (self, load):
        pass
    @property
    @abstractmethod
    def fuel (self):
        pass

    @fuel.setter
    @abstractmethod
    def fuel (self, amount):
        pass

class Honda (Car):
        def __init__(self):
            self.speed = 0
            self._fuel = 0
        def show_speed (self):
            print (self.speed)
        def change_speed (self, speed):
            if speed > 0:
                needed_fuel = speed * 2
                if self.fuel < needed_fuel:
                    print("Out of fuel")
                    self.speed = 0
                else:
                    self.speed += speed
                    self.fuel -= needed_fuel

            elif speed < 0:  #
                self.speed += speed
                if self.speed < 0:
                    self.speed = 0

        def load_fuel (self, load):
            self.fuel = self.fuel + load
        def show_fuel (self):
            print (self.fuel)

        @property
        def fuel (self):
            return self._fuel

        @fuel.setter
        def fuel (self, amount):
            if amount < 0:
                print ('Out of fuel')
                self._fuel = 0
                self.speed = 0
            else:
                self._fuel = amount

amin = Honda ()

amin.fuel  = 100
amin.show_fuel()

amin.change_speed(20)
amin.show_speed()
amin.show_fuel()
amin.change_speed(10)
amin.show_speed()
amin.show_fuel()
amin.change_speed(-30)
amin.show_speed()
amin.show_fuel()

amin.change_speed(30)
amin.show_speed()
amin.show_fuel()
