
#TASK

#This code is to directly apply at nested-list problem in python in HACKERRANK

#Given the names and grades for each student in a Physics class of N students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, 
#order their names alphabetically and print each name on a new line.



#CODE

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    
score_list = []
mark_sheet = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    mark_sheet.append([name,score])
    score_list.append(score)

second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]    #avoiding duplications and sorting the list

for name,marks in sorted(mark_sheet):
    if marks == second_lowest_mark:
        print(name)
	
#ENJOY
