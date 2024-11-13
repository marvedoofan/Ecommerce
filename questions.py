# program for counting odd and even numbers
from itertools import count
import numbers


count_even = 0
count_odd = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for number in numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("EVEN NUMBERS ARE:", + count_even)
print("ODD NUMBERS ARE:", + count_odd)
# question number 5 a GLOBAL AND LOCAL VARIABLES
a = 1
def_varname():
return a+1
print(varname1)
