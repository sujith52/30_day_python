import csv

with open('people.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name","grade"])
    writer.writerow(["sujith",88])
    writer.writerow(["sreeja",74])
    writer.writerow([ "lalitha",74])

with open('people.csv',mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#   challenge 2

with open("marks.csv","w",newline="") as file:
    wr = csv.writer(file)
    wr.writerow(["name","maths","science","english"])
    wr.writerow(["sujith",88,92,85])
    wr.writerow(["sreej",78,83,85])
    wr.writerow(["lalith",90,87,88])

with open('marks.csv',mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#   challenge 3

with open("marks.csv","r") as file:
    read = csv.reader(file)
    next(read)
    for row in read:
        name = row[0]
        marks = list(map(int,row[1:]))
        avg = sum(marks) / len(marks)
        print(f"Name is {name} - Average marks : {round(avg,1)}")

#   challenge 4

new = ['vinitha',85,90,91]

with open("marks.csv","a",newline='') as file:
    writ = csv.writer(file)
    writ.writerow(new)

# i completed it on 08-05-2025 on 07:58 am
#  i think it need 7  more sessions