#Setter is to modify and update the value with validation
#Getter is to retrieve and return the data
#'_' for protect variable (can access within its class and subcalss)
#'__" for private variable (Can access only within its class, use Getter and Setter)

#Encapsulation refers to the process of wrapping data and methods together inside a (class)
# while restricting direct access to some details.

'''class Exam:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks! Must be betwen 0 and 100.")

#creating object
exam1=Exam("Ali", 90)

#Using Getter
print("Marks: ", exam1.get_marks())

#Using setter
exam1.set_marks(85)
print("Updated Marks: ", exam1.get_marks())

#Trying Invalid value
exam1.set_marks(-10)

'''
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

#getter method(to read private data)
    def get_balance(self):
        return self.__balance

#Setter method(to update private data with conditions)
    def set_balance(self, new_balance):
        if new_balance >= 0:
           self.__balance = new_balance
        else:
           print("Balance cannot be negative!")

    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited: {amount}, New balance: {self.__balance}")

    def withdraw(self,amount):
        if amount <= self.__balance:
           self.__balance -= amount
           print(f"Withdrawn: {amount}, Remaining balance: {self.__balance}")
        else:
           print("Insufficient balance!")
account = BankAccount(5000)
#trying to accept private variable directly will fail
#print(account.__balance)

#Using getter to access private data
print(account.get_balance())

#Using setter to modify private data
account.set_balance(7000)
print(account.get_balance())

