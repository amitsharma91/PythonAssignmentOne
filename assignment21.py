"""
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
"""

import sys

num = input("Enter Number to print table: ")

i=1
while(i<=10):
	print("%d x %d = %d" % (num,i,num*i))
	i+=1
#end of while
