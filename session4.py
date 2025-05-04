# if, elif, and else statements are used for this purpose:
# 1:49 right now i was madly hungry but i still cooking code
# challeng 1
print("Enter your marks:")
mat = input("Enter maths marks:")
phy = input("enter physics marks:")
chem = input("Enter physics marks:")
mat = int(mat)
chem = int(chem)
phy = int(phy)
total = mat+chem+phy
print("Total marks is :",total)
if total >=90:
    print("Grade A, topper")
elif 89> total >75:
    print("Grade b")
elif 74> total >50:
    print("Grade c")
elif total >20:
    print("failed sucessfully")

#  correct code is
print("Enter your marks:")

mat = input("Enter maths marks: ")
phy = input("Enter physics marks: ")
chem = input("Enter chemistry marks: ")

mat = int(mat)
phy = int(phy)
chem = int(chem)

total = mat + phy + chem
print("Total marks is:", total)

if total >= 90:
    print("Grade A, topper")
elif total >= 75 and total < 90:
    print("Grade B")
elif total >= 50 and total < 75:
    print("Grade C")
elif total >= 20 and total < 50:
    print("Failed successfully")
else:
    print("Invalid marks")

