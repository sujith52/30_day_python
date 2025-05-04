#  Session 3: Data Types
name = input("enter the name: ")
age = input("age is ")
m1 = input("Maths marks ")
sci = input("physics marks ")
eng = input("Chemistry marks ")
host = input("are you a hosteller (yes/no)") == "yes"
m1= int(m1)
sci= int(sci)
eng = int(eng)
marks =(m1+sci+eng)/3
print("average marks is ",marks)

# this session made me to get hungry 
# man of my words  time is 1:16pm i done arount 1 hourof coding

#           challenge 1

name = input("enter the full name :")
age = input("age is :")
gender = input("Your Gender:")
cont = input("Contact Number:")
m1 = input("Maths marks :")
sci = input("Science marks :")
eng = input("English marks :")
m1= int(m1)
sci= int(sci)
eng = int(eng)
marks =(m1+sci+eng)/3
print("average marks is ",marks)

print("Hello Yoo Yoo ",name)
if marks<60:
    print("You are passing also cooking")
else:
    print("Your life is runied now")
print('\n maths marks',m1)
print("sciense marks",sci)
print("English marks",eng)
print("Average marks is ",marks)


#               challeng 2
epname = input("Enter Employee name :")
sal = input("Enter your basic salary:")
hra = input("Enter your HRA:")
da = input("Enter your DA:")
sal = float(sal)
hra = float(hra)
da = float(da)
gs = sal+hra+da
print("Gross salary",gs)
if gs <50000:
    print("exceeded treshold minimum")
else:
    print("You are poor")


#               challeng 3
ori = input("Enter Original price of item:")
ori = float(ori)
dis = input("Enter discount :")
dis = int(dis)
final = ori-dis
print("original :",ori)
print("discount :",dis)
print("final price",final)

#               challenge 3 answer
ori = input("Enter Original price of item: ")
ori = float(ori)

# Taking the discount as a percentage
dis = input("Enter discount percentage: ")
dis = int(dis)

# Calculating the discount value
discount_value = (ori * dis) / 100

# Calculating the final price after discount
final = ori - discount_value

# Printing results
print("\nOriginal Price: ", ori)
print("Discount Percentage: ", dis, "%")
print("Discount Value: ", discount_value)
print("Final Price: ", final)
