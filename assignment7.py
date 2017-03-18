"""
Write a Python program to get the Fibonacci series.
"""

import sys

limit = input("Enter the Limit: ")

curr = 1;
next = 1;

sys.stdout.write("Fibonacci Series upto "+str(limit)+" is: ")
while(curr <= limit):
    #print(curr)#prints in new-line
    sys.stdout.write(str(curr)+' ')#to print in One Line
    temp = curr
    curr = next
    next = temp + next
# end of While-Loop

print("")
