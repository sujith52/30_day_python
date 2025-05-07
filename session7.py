# 04-05-2025 12:59 i watched a lot of hell of tutorials
# i will not stuck in tutorial hell so i will work on

na = input("Enter your full name :")
print("Uppercase :",na.upper())
print("Lowercase :",na.lower())
print("Title Case :",na.title())

#       challenge 2
st = input("Enter the scentence :")
vo = "aeiouAEIOU"
count = 0

for char in st:
    if char in vo:
        count += 1
print("Number of vowels :",count)

#       challenge 3

fir = input("Enter the user first name :")
las = input("Enter  the user last name :")
print("Your user name is :",fir[0:4]+las[0:4])

#       challenge 4
wor = input("Enter the word :")
if wor == wor[::-1]:
    print("it is a palindrome")
else:
    print("It never been")
