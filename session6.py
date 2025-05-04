# Session 5: Loops – While Loops and Nested Loops
# 12:39 it was a haard session

# count = 10
# while count>=1:
#     print(count)
#     count -= 1
# print("Lift off")

#       today 04-05-2025
# 15 percent of the data analysit course i completed now python 

#   challenge 2
# num = 1
# total =0
# while num <= 400:
#     if num % 2 == 0:
#         total += num
#     num += 1
# print("The sum of nums from 1 to 50 are ;",total)

#   challeng 3
# for i in range (1,5):
#     for j in range(1,11):
#         print(i,'x',j,'=',i*j)
#     print("------------")

#   challenge 4
# i = 1
# while i<=4:
#     j=1
#     while j<= i:
#         print('*',end=" ")
#         j+=1
#     print()
#     i+=1

#   challenge 5

import random

secret = random.randint(1,10)
guess = 0

while guess != secret:
    guess = int(input("Enter Secret Num from 1 to 10 :"))
    if guess == secret:
        print("Correct guess")
    else:
        print("Wrong try again")