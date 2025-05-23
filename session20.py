
# today 10-05-2025 01:01 pm 
#my motivation is not good


import json

data =' {"name":"sujith", "age":21,"course":"datascience"}'
js_data = json.loads(data)
print(js_data["name"])

#   challenge 1

data = {"name":"suji","age":21,"marks":560}
js_data = json.dumps(data)
print(js_data)

#   challenge 2

student_json = '{"name": "Jeevan", "age": 22, "course": "AI"}'
js = json.loads(student_json)
print(js["name"])
print(js["age"])

#    challenge 3
data = {"shutter ":":island","inception":"oppenhemier","man of":" steel"}
with open("movie.json","r") as file:
    m = json.load(file)
    print(m)

#   challenge 4

import json

people = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "London"},
    {"name": "Charlie", "age": 22, "city": "Delhi"}
]

with open("people.json", "w") as f:
    json.dump(people, f)


#   mistakes happen 

import json

data = {"name":"sujith","age":21}
print_saion = json.dumps(data)
print(print_saion)

#   chal2

student =' {"name":"sujith","age":21,"course":"AI&Data science"}'
dicts = json.loads(student)
print("Nmae",dicts["name"])
print("Age",dicts["age"])
print("course",dicts["course"])

#   challenge 3

movie = {
    "title":"shutter island ",
    "director":"cristoper nolan",
    "year":2010
}

