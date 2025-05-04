name = input('Enter your name :')
age = input('enter yor age:')

str(name)
age = int(age)
print('hello ',name+', next year your age will be ',age+1,'years old')

            # mediumchallenge 2nd may 2025

name = input("Enter the name  ")
college= input("Enter the college   ")
branch= input("Enter the branch  ")
year= input("Enter the year   ")
percentage= input("Enter the percentage ")
percentage = float(percentage)
if(percentage>=75):
    print("Excellent performance!")
elif(percentage<=74):
    print("Good job bro you are cooked")
else:
    print("work hard")
print('hello ',name)
print('You are studying in ',college,'college', branch,' branch.')
print('you are in ',year,'year')
print("your percentage is ",percentage)

        # correct outcome is
name = input("Enter your name: ")
college = input("Enter your college: ")
branch = input("Enter your branch: ")
year = input("Enter your year of study: ")
percentage = float(input("Enter your percentage: "))

print("\nHello", name + "!")
print("You are studying in", college + ",", branch, "branch.")
print("You are in your", year, "year.")
print("Your current percentage is", percentage, "%")

# Feedback based on performance
if percentage >= 75:
    print("Excellent performance!")
elif 60 <= percentage < 75:
    print("Good job, keep improving!")
else:
    print("You need to work harder!")

# i am cooked