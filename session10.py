
#   challenge 1
student = {
    "name":"Sujith Kumar ",
    "age":21,
    "branch":"CSE"
}
print(student)
student["GPA"] = 7.7
student["branch"]="CSE(GENRAL)"
print(student)

# challeng2

inventory ={
    "apples":12,
    "banana":10,
    "milk":2
}
inventory["bread"]=4
print(inventory["banana"])

# ccha4

person = {
    "name": "Amit",
    "city": "Delhi",
    "age": 24
}
for key,value in person.items():
    print("Key",key,"Value",value)

word = "programming"
letter_count = {}
# ch3
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)

