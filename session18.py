# Session 18: Introduction to File Handling

# 07-05-2025 08:20 am 
# i think it was last sessionn next we will meet in projects

#       challenge 1

f = open("user_input.txt","w")
content = input("Enter the Text you want to enter :")
f.write(content)
f.close()

f = open("user_input.txt","r")
content = f.read()
print(content)
f.close

#       challenge 2

with open("user_input.txt","r") as file:
    for line in file:
        print(line.strip())

#   challeneg 3
f = open("fruts.txt","w")
f.write("mango\norange\nguva\nhaaaa\npanasakaya\ngannerukaya")
f.close()

with open("fruts.txt","a") as file:
    file.write("\ngrapes")

f=open("fruts.txt","r")
f.read("fruts.txt")
f.close()

#   challeneg 5

with open("fruits.txt", "r") as source:
    data = source.read()

with open("copied_fruits.txt", "w") as target:
    target.write(data)
