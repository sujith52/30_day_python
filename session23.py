import csv
import os

filename = 'scores.csv'
file_exists = os.path.isfile(filename)

name = input("Enter your name: ")
score = input("Enter your score: ")

with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(['Name', 'Score'])  # write header only once
    writer.writerow([name, score])
print("Data saved to scores.csv")



import csv

total = 0
count = 0

with open('student.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        total += int(row[1])
        count += 1

if count > 0:
    average = total / count
    print("Average Marks:", average)
else:
    print("No student data found.")


import pandas as pd

df = pd.read_csv('student.csv')
filtered = df[df['age'] > 80]

print("Students with marks > 80:")
print(filtered['name'].to_string(index=False))
