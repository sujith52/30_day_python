import pandas as pd

df = pd.read_csv('students.csv')

print(df.head())
print(df.columns)
print("shape ",df.shape)

print(df.dropna())
print(df.drop_duplicates())

print("Average marks of subject",df.groupby("Subject")["Marks"].mean())
print("Average marks of subject",df["Grade"].value_counts())
print(df["Marks"]<50)

def count_by_grade(grade):
    return len(df[df['Grade'] == grade])

grade = input("Enter the grade:")
print("Students with Grade A:", count_by_grade(grade))

import matplotlib.pyplot as plt

plt.hist(df['Marks'],bins=5,color='skyblue')
plt.title("Bar graph show casing the marks ")
plt.xlabel("Marks")
plt.ylabel("No of students ")
plt.show()

plt.bar(df["Grade"])
plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()



grade_counts = df["Grade"].value_counts()

plt.bar(grade_counts.index, grade_counts.values)
plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()
