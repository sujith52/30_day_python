import json

data = {"name": "Sujith", "age": 21, "skills": ["Python", "SQL"]}
read = json.dumps(data)
print(read)

#   challenge 2

data = '{"name": "Sujith", "age": 21, "skills": ["Python", "SQL"]}'
read = json.loads(data)
print("json data",read)

#   chal 3

clgdetails = {
    "Name":"Aditya clg of Eng (ACEM)",
    "Location":"madanapalle",
    "Grade":"Affliated to JNTUA , Anathapuram"
}

with open("college.json",'w')as file:
    json.dump(clgdetails,file)

#   chal 4


with open("college.json",'r')as file:
    data= json.load(file)

print("College name is ",data["Name"])
print("College location ",data["Location"])

#   chal 5

st1 = {
    'name':"sujii",
    'roll':"5A4",
    "garde":"c"
}

st2 = {
    'name':"sreju",
    'roll':"599",
    "garde":"A"
}

st3 = {
    'name':"lallu",
    'roll':"59",
    "garde":"A"
}

with open("students.json","w",newline='') as file:
    json.dump(st1,file)
    json.dump(st2,file)
    json.dump(st3,file)