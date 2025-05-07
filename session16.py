#  Session 16: Classes and Inheritance
# it was 06-05-2025 10:44 am
# i can say that consistency at the peak 

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(self.name,"makes sound ")

# class Dog(Animal):
#     def speak(self):
#         print(self.name," Syas WOOf")

# d = Dog("Oliver")
# d.speak()

#   challenge 1
# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def displa_info(self):
#         print("NAME IS ",self.name)
#         print("AGE IS ",self.age)
#         print("Grade is  ",self.grade)

# sl = Student("Sujith",21,"A")
# sl.displa_info()

#   challenge 2

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Added sucessfully ")
        print("The balance is ",self.balance)

    def withdraw(self,amount):
        self.balance -=amount
        print("Withdrawed sucessfully")
        print("The balance is ",self.balance)

    def display_balance(self):
        print("The account holder is  ",self.account_holder)
        print("The balance is ",self.balance)
        
ba = BankAccount("SUJITH",2000)
ba.deposit(200)
ba.withdraw(1000)
ba.display_balance()


#       challenge 3

class Vechile:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print("..",self.brand)

class Car(Vechile):
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    def start(self):
        print(f"The {self.brand} {self.model} is strting ")

c = Car("7500RPM","Frod")
c.start()


#       challenge 4
class Calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
    
a = int(input("A Value ::"))
b= int(input("B Value ::"))
c = Calculator()
c.add(a,b)
c.sub(a,b)
c.mul(a,b)
c.div(a,b)

#      challnege 4


class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()


# i have completed it on 11:22 am 
# so i took hour 
# keep fighting we woll make it 