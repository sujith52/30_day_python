# Session 15: Object-Oriented Programming (OOP) Basics.
# still i need to complete 4 more 
# 05-05-2025 2:59 pm 

# challenge 1

class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"The car is {self.brand}, its model is {self.model}, it was realeased in {self.year}")

car1 = car("Frod","7500RPM",1999)
car1.display_info()

#   challenge 2

class student:
    def __init__(self,name,maths,science,english):
        self.name = name 
        self.maths =maths
        self.science = science
        self.english = english
    def average(self):
        c = self.maths + self.science  + self.english  
        d = c/3
        print("The average is :",c)
        print("Your name is ",name)

name = input("Enter name  ")
maths =int(input("Enter maths   "))
science = int(input("Enter science  "))
english = int(input("Enter english  "))
st1 = student(name,maths,science,english)
print(st1.average())


#       challenge 3

class bankaccount:
    def __init__(self,owner,balance):
        self.ownwer = owner
        self.balance = balance
    def deposit(amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(amount):
        amount = self.balance+amount
        return amount
owner=input("Enter name :")
balance = int(input("Enter the balance :"))

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

# Example usage:
acc = BankAccount("Sujith", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)

#   challenge 4

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def summary(self):
        print(f"Book : {self.title} by {self.author}, {self.pages} .")

crf = Book("Wings of fire ","APJ Abdul Kalam ",369)
print(crf.summary())
        
