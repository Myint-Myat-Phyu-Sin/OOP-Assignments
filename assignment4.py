#Myint Myat Phyu Sin
#ID - 68111400

#Exercise - 1
class Inventory:
    def __init__(self,product_name,stock):
        self.__product_name = product_name
        self.__stock = stock

#Use getter to access the variable
    def get_stock(self):
        return self.__stock

#Use setter to update the variable with conditions
    def set_stock(self,stock):
        if stock >= 0:
            self.__stock = stock
        else:
           print("Invalid stock!")

    def sell(self,quantity):
        if self.__stock >= quantity >= 0:
           self.__stock -= quantity
        else:
           print("Insufficient stock!")
    def restock(self,quantity):
        if quantity >= 0:
           self.__stock += quantity

p = Inventory("Laptop",20)
p.sell(8)
print(p.get_stock())
p.sell(15)
p.restock(10)
print(p.get_stock())
p.set_stock(-5)
print(p.get_stock())

#Exercise - 2
class Course:
    def __init__(self,capacity):
        self.__capacity = capacity
        self.__enrolled = 0

    def get_capacity(self):
        return self.__capacity
    def get_enrolled(self):
        return self.__enrolled
    def set_capacity(self,new_capacity):
        if new_capacity > 0  and new_capacity >= self.__enrolled:
            self.__capacity = new_capacity
        else:
           print("Cannot reduce capacity below enrolled students!")

    def enroll_students(self,numbers):
        if self.__capacity >= self.__enrolled + numbers and numbers > 0:
            self.__enrolled += numbers
        else:
            print("Not enough seats!")
    def drop_students(self,numbers):
        if self.__enrolled >= numbers > 0:
            self.__enrolled -= numbers

course =Course(5)
course.enroll_students(3)
print(course.get_enrolled())
course.set_capacity(2)
course.enroll_students(3)
course.drop_students(1)
course.set_capacity(2)
print(course.get_capacity())
print(course.get_enrolled())

#Exercise - 3
class ElectricityBill:
    def __init__(self,units):
       self.__units = units
    @property
    def units(self):
       return self.__units
    @units.setter
    def units(self,new_units):
       if new_units >= 0:
          self.__units = new_units
       else:
           print("Invalid Units!")
    @property
    def total_bill(self):
        if 0 < self.__units <= 100:
           return self.__units * 5
        elif self.__units <= 200:
            return (100 * 5)  + ((self.__units - 100) * 7)
        else:
            return (100 * 5)  +  (100 * 7) + ((self.__units - 200) * 10)
bill = ElectricityBill(80)
print(bill.total_bill)
bill.units = 250
print(bill.total_bill)
bill.units = -10
print(bill.units)

#Exercise - 4
#Used method parameters instead of Constructor parametrs
class ShoppingCart:
    def __init__(self):
       self.__subtotal = 0
       self.__discount = 0

    def add_item(self, price, quantity):
        if price <= 0 or quantity <= 0:
           print("Price and quantity must be positive!")
        self.__subtotal += price * quantity
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self,new_discount):
        if 0 <= new_discount <= 30:
            self.__discount = new_discount
        else:
            print("Invalid discount!")

    @property
    def total(self):
        return self.__subtotal * (1 - self.__discount / 100)
cart = ShoppingCart()

cart.add_item(1000, 2)
cart.add_item(500, 1)
cart.discount = 20
print(cart.total)
cart.discount = 40
cart.add_item(200, 1)
print(cart.total)

#Exercise - 5
class BusTicket:
    def __init__(self,age,distance):
        self.__age = age
        self.__distance = distance

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if 0 <= new_age <= 120:
            self.__age = new_age
        else:
            print("Invalid age!")

    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self,new_distance):
        if new_distance > 0:
            self.__distance = new_distance
        else:
            print("Invalid distance!")

    @property
    def fare(self):
        if self.__age <= 5:
            return 0
        elif 6 <= self.__age <= 12 or self.__age >= 60:
            return (10 + self.__distance * 5) / 2
        else:
            return 10 + self.__distance * 5

ticket = BusTicket(25, 10)
print(ticket.fare)
ticket.age =65
print(ticket.fare)
ticket.distance = -5
print(ticket.fare)
ticket.age =4
print(ticket.fare)
#age and distance need setters because users may update their age or travel distance
#fare should be read-only because it is automatically calculated using age and distance


