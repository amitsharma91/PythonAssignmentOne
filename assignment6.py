"""
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue&' statement. 
Expected Output : 0 1 2 4 5
"""
import sys

sys.stdout.write("0 ")
for i in range(0,7):
	if(i%3==0):
		continue;
	sys.stdout.write(str(i)+" ")
#end of For
print("")
