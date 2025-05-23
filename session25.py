import pandas as pd

data = {
    'name':['sujith','sreevan','lalitha',None],
    'age':[22,23,None,19]
}

df = pd.DataFrame(data)

print(df.dropna())
print(df.isnull)
print(df.fillna("Gone "))
print(df.fillna("Dont know"))


data = pd.DataFrame({
    'name':['sujith','sujith','sreevan','lalitha',None],
    'age':[22,22,23,None,19]
})

data = data.drop_duplicates()

print(data)

data = {
    'name':['sujith','sreevan','lalitha',None],
    'age':[22,23,None,19]
}
df = pd.DataFrame(data)

df.rename(columns={'age':'ReaalAge'},inplace = True)
print(df)

df['age'] = pd.to_numeric(df['age'], errors='coerce')  
print(df)

df = pd.DataFrame({
    'Age': ['25', '30', 'NaN', '45']
})

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  

print("Converted column:\n", df)
