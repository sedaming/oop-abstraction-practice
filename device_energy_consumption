from abc import ABC, abstractmethod

class Device (ABC):

    @property
    @abstractmethod
    def battery_level (self):
        pass
    @battery_level.setter
    @abstractmethod
    def battery_level (self, charge):
        pass
    @abstractmethod
    def use(self, hours):
        pass

class Phone (Device):
    def __init__(self, ph_level):
        self.ph_level = 0
        self.battery_level = ph_level


    @property
    def battery_level(self):
        return self.ph_level
    @battery_level.setter
    def battery_level(self, charge):
        if charge > 100:
            self.ph_level = 100
            print('invalid')
        elif charge < 0:
            self.ph_level = 0
            print ('invalid')
        else:
            self.ph_level = charge

    def use(self, hours):
        new_level = self.battery_level - (hours * 10)
        if new_level <0:
            self.battery_level = 0
        else:
            self.battery_level    = new_level




class Laptop (Device):
    def __init__(self, lp_level):
        self.lp_level = 0
        self.battery_level = lp_level


    @property
    def battery_level(self):
        return self.lp_level
    @battery_level.setter
    def battery_level(self, charge):
        if charge > 100:
            self.lp_level = 100
            print('invalid')
        elif charge < 0:
            self.lp_level = 0
            print ('invalid')
        else:
            self.lp_level = charge

    def use(self, hours):
        new_level = self.battery_level - (hours * 15)
        if new_level <0:
            self.battery_level = 0
        else:
            self.battery_level = new_level

p = Phone (120)
print (p.battery_level)

p = Phone (-90)
print (p.battery_level)


l = Laptop (60)
print (l.battery_level)
l.battery_level = 70
print (l.battery_level)
