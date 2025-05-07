#  Session 14: Error Handling and Exceptions.
# i thinkit was last then we will focus on excel operations then power bi
# exiciting journey ahead
# 05-05-2025 8:44 am 

vi = int(input("Enter numerator :"))
vl = int(input("Enter the denominator :"))
try:
    x=vi/vl
except ZeroDivisionError:
    print("It cant divided by zero.")

#   challenge 2

age = int(input("Enter the age now :"))
try:
    print(age)
except ValueError:
    print("It is in string")

#   challenge 3

num = int(input("Enter number :"))
div = int(input("Enter div :"))
try:
    c = num/div
    print(c)
except ValueError:
    print("it is nor string ")
except ZeroDivisionError:
    print("Its value is zero ")
   
#   challenge 3
f = open("myfile.txt","w")
f.write("Its a great pleasure to meet yoy\n the github spyer \n how was my profile")
f.close()

try:
    f = open("myfile.txt","r")
    f.close()
    print(f)
    print("file found")
except FileNotFoundError:
    print("The filr didnt found ")

# challenge 5

vs = int(input("Enter a :"))
vl = int(input("Enter b :"))
try:
    c = vs/vl
    print("answer is ",c)
except ValueError:
    print("The string is entered ")
finally:
    print("Thankyou for finding and using our calculator //")