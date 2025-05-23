import pandas as pd

df = pd.read_csv("student.csv")

#   chal 1
print(df.head())

# chal 2

print(df[["name","marks"]])
#   chal 3
high = df[df["marks"]>20]
print(high)

#   chal 4
def assign(marks):
    if marks>=25:
        return 'A'
    elif marks >=20:
        return 'B'
    else:
        return 'Fail'
    
df["grades"] = df["marks"].apply(assign)

print(df)

#   chal 5

df.to_csv("graded_students.csv", index=False)
print("Data frame has been saved successfully !!")