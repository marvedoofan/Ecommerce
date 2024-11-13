

print("hello world")
print('paul\'s book')
print(r"c:user\paul\musics\new")
# variables
# concatination
# myname = "Blessing"
# age = 28
# print("my name is", + myname, " i am +age, years old. i got the name blessing when i was young.")
# index
# myname = "Francis"
# print(myname)
# print(myname[3])
#
# print(myname[3:7])
# print(myname[:4])
# print(myname[:3])
# length of strings
# a string is a combination of characters
myname = ("my name is Francis")
print(len(myname))
print(myname[3])
# list
food = ["Rice", "beans", "akpu", "chinken"]
print(food)
print(type(food))
# if you want to replace beans with garri in the list
food[1] = "Garri"
print(food)
# LIST INSIDE A LIST i.e function of a function
courses = ["MTH", "STA", ["cmp 201", "cmp223", "cmp205"],]
print(courses)
# list methods is the process of manipulating a list e.g either you want to add or remove smthing frm a list
# append() adds smthing to a list
food.append("indomie")
print(food)
# clear() will clear the whole list nd give an empty list
# food.clear()
print(food)
# insert
food.insert(2, "meat")
print(food)
# pop() will remove the last list that was added
