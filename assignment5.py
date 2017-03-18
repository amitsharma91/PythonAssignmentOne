"""
Write a Python program to count the number of even and odd numbers from a series of numbers. 
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output : 
Number of even numbers : 5
Number of odd numbers : 4
"""

import sys

ev = 0;
od = 0;
tup = (1,2,3,4,5,6,7,8,9)

print("Tuple elements are: ")
for n in tup:
	sys.stdout.write(str(n)+" ")	
	if(n%2==0):
		ev+=1;
	else:
		od+=1;
#end of for

print("\nNumber of even numbers :%d" % ev)
print("Number of odd numbers :%d" % od)
