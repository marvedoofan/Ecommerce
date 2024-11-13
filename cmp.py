import time
print("This is computer Programming 1")

# assigning values to Variables
a = 2
b = 4
name = "Peace"
print(a, b, name)
# multiple assignment of values to var
a, b, c = 2, 4, "peace"
print(a)
print(b)
print(c)
# for loop syntax
count = 0
for i in range(5):
    count = i+count

    print(i)
# while loop executes a statement as long as condition is true
i = 1
while i < 6:
    print(i)
    i += 1
 # break statements are used to stop a loop eventhough while condition is true
i = 1
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1    # number 1
