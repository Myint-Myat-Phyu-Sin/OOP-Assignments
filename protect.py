#Protected attributes can be accessed inside subclasses but should not
#be modified directly.
class Car:
    def __init__(self,brand,speed):
        self._brand = brand  #protected variable
        self._speed = speed  #protected variable

class SportCar(Car):
    def show_details(self):
        print(f" Brand : {self._brand}, Speed : {self._speed}")
car1 = SportCar("Sport",100)
car1.show_details()          #Accessible inside subclass