# Session 17: Advanced Object-Oriented Programming (OOP).

class book:
    def __init__(self,title,author):
        self.title = title 
        self.author = author
    def __str__(self):
        return f"Book : {self.title} and author {self.author}"

b = book("Wings of fire","APJ Kalam")
print(b)
        

#       challenge 2

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        print("Added sucessfully ")
        print("The balance is ",self.__balance)

    def withdraw(self,amount):
        self.__balance -=amount
        print("Withdrawed sucessfully")
        print("The balance is ",self.__balance)

    def display_balance(self):
        print("The account holder is  ",self.account_holder)
        print("The balance is ",self.__balance)
        
ba = BankAccount("SUJITH",2000)
ba.deposit(200)
ba.withdraw(1000)
ba.display_balance()

#   challenge 3

class vechile:
    def __init__(self,brand):
        self.brand = brand
    
class car(vechile):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model 

    def display(self):
        print(f"Brand :{self.brand} ,Model : {self.model}")

cl = car("Frod","7500RPM")
print(cl.display())

#   challenge 4

class Cat:
    def make_sound(self):
        print("Meow")
    
class Dog:
    def make_sound(self):
        print("Boww")
animals = [Cat(),Dog()]
for animal in animals:
    animal.make_sound()
        

#   challenge 5

class Student:
    school_name = "XYZ School"  # class attribute

    def __init__(self, student_name):
        self.student_name = student_name  # instance attribute

s1 = Student("Alice")
s2 = Student("Bob")

print(f"{s1.student_name} studies at {s1.school_name}")
print(f"{s2.student_name} studies at {s2.school_name}")

# i think it was the end of the the session practice 
# 07-05-2025 on this day i completed all 18 sessions practice
# each session took me almost 30 to 50 minutes
# keep fighting 
# until death defeat is pyscological 