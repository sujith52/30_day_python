import pandas as pd

df = pd.read_csv("student.csv")
print(df.head())
print("No of columns :",df.columns.to_list())
print("Shape",df.shape)

print(df.describe())
print("Average Marks",df["Marks"].mean())

print("Grade Counts \n ",df["Grade"].value_counts())
print("Uniique ",df["Grade"].unique())

print("Scored more than 85",df[df["Marks"]>85])
print("Younger than 22",df[df["Age"]<22])

print("Average Grade:",df["Grade"].mean())
print("Average Marks per Grade:\n", df.groupby("Grade")["Marks"].mean())
print("Student Count per Grade:\n", df.groupby("Grade")["Name"].count())


import matplotlib.pyplot as plt
df["Marks"].hist()
plt.title("Marks of all the tsudents")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

df["Grade"].value_counts().plot(kind='bar', color='skyblue')
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Count")
plt.show()