from itertools import count
import time


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# program to check for voting
print("program to check for voting")
print("enter your age")
age = int(input())
if age >= 18:
    print("Yo are eligible for voting")
else:
    print("Sorry you are not eligible for voting")
    print(age)
# program of a simple game
print("GET READY FOR THE GAME..!!")
for i in range(5, 0, -1):
    print(i)
time.sleep(1)
print("START..!!")
