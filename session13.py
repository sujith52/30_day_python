f = open("Example.txt","w")
f.write("Hello dark world this is my first file in python i am supper exited. \n")
f.write("File handling must be fun right ??")
f.close

#   challenge 1

f = open("Diary.txt","r")
f.write("Today is 05-05-2025 \n i am feeling very good \n i am thing about watching the old boy film ")
f.write("i am also reading swallowed star fan friction \n")
content = f.read()
print(content)
f.close

# challenge 2

f = open("poem.txt","w")

f.write("her eyes are stars \n her words are music \n but why did she left me \n all is decided by fate why bother?")

with open("poem.txt","r") as f:
    lines = f.readlines()
    print(lines)
    print("Number of lines :",len(lines))
f.close()

#        challenge 3
mood = input("How the hell are you felling today?? :")
with open("mood_log.txt","a") as f:
    f.write(mood + "\n")
print(f'"{mood}" has been logged')

#   challenge 4

f = open("story.txt","w")
f.write("Hello here is immortal story \n wahha wahhha")
with open("story.txt","r") as f:
    story = f.read()

up_story = story.replace("boring","exicing")

with open("story.txt","w") as f:
    f.write(up_story)
print("Words has been replaced and saved to up_story.txt")

#   challenge 5

f = open("notes.txt","w")
f.write("heloo to the helled world \n hi ")
f.close()

with open("notes.txt","r") as source:
    content = source.read()
with open("backup_notes.txt","w") as backup:
    backup.write(content)
print("The file copied sucessfully")