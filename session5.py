#  Session 5: Loops in Python.
# today 03-05-2025 12:04 am lets wrap the first plan of the session list i.e basiscs of python
# 
for i in range(10):
    print(i)
    i +=1
    if i==5:
        print("Found 5")
        break
    
#               challeng 1
for i in range(21):
    if i == 14:
        continue
    if i %2==0:
        print(i)

#           challeng 3


for i in range(1,11):
    num = int(input("Enter any number between 1 and 10 :"))
    if i == num:
        print("The Entered num has Found")
        continue
    print(i)


num = int(input("Enter any number between 1 and 10: "))
for i in range(1, 11):
      # Convert input to int
    if i == num:
        print("The Entered number has been found!",i,'.')
        continue  # Skip the current value of i
    print(i)

#           challenge 3
for i in range(100):
    i = i+1
    print(i)
    if i >= 100:
        break

total =0
for i in range(1,100):
    total += i
    if total >= 100:
        break
print("final sum is ",total)
