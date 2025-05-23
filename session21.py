import csv

with open("student.csv","w")as file:
    wr = csv.writer(file)
    wr.writerow(["name","age","grade"])
    wr.writerow(["alice",20,"A"])
    wr.writerow(["bob",23,"AAAAA"])
    wr.writerow(["chap",24,"AA"])
    wr.writerow(["pal",27,"AAA"])

with open("student.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#   challenge 2

with open("student.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(len(row))

#   challenge 3

with open("student.csv","r")as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['grade'] == 'A':
            print(row)

#   challenge 4

data = [
    ['name', 'score'],
    ['Ravi', 85],
    ['Anjali', 92],
    ['Meena', 78]
]

with open("scores.csv","w") as file:
    read = csv.writer(file)
    read.writerows(data)


#   challenge 5

name = input("Enter Your name MR ::")
score = input("Enter your score sir ::")
with open("scores.csv","a",newline='') as file:
    write = csv.writer(file)
    write.writerows([name,score])