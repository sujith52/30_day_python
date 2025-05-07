# Session 11: Functions in Python
# i think i basically completed 50% in python
# exiciting soon i will able to reach my goal 

def greet_user(name):
    print("Hello, ",name,"Welcome !")
name = input("Enter name please :")
greet_user(name)

# chal2

def mul(a,b):
   return a * b

a = int(input("Enter value of a"))
b = int(input("Enter value of b"))
vis = mul(a,b)
print(vis)

# char3

def check_even(num):
    if num % 2 == 0:
        print("Its even")
    else:
        print("ODD")
num = input("Enter NUm ")
check_even(num)

# chal4

def average(m1,m2,m3):
    return  (m1+m2+m3)/3
m1 = int(input("Enter m1 value"))
m2 = int(input("Enter m2 value"))
m3 = int(input("Enter m3 value"))
iso = average(m1,m2,m3)
print(iso)

# chal5

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial is:", factorial(6))

# 🎉 Progress Update:
# Yes, you're right! You're around 50% through core Python
#finally i completed pyhon fundamentals then 
# now we will drive into  advanced