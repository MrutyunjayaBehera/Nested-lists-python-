import math
import os
import random
import re
import sys


"""n = input("enter the  number: ")
n = int(n)

if n % 2 != 0:
	print("Weird")
else:
	if n > 2 and n < 5:
		print("Not Weird")
	elif n > 6 and n < 20:
		print("Weird")
	elif n > 20:
		print("Not Weird")"""

"""n = input("enter the number: ")
n = int(n)
for i in range(1,n+1):
    print(i, end = "")"""

"""x = input("raw_input1: ")
x = int(x)
y = input("raw_input2: ")
y = int(y) 
z = input("raw_input3: ")
z = int(z)
n = input("raw_input4: ")
n = int(n)

print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n])"""

k = input()
arr = []
arr = k.split(" ")
print(arr)

large = max(arr)
n = len(arr)
for i in range(n):
	if large == max(arr):
		arr.remove(max(arr))
print(max(arr))
