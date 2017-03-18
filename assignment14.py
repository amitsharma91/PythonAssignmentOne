"""
Write a Python program to check a string represent an integer or not
Expected Output
Input a string Python                                                  
The string is not an integer.
"""

import sys

strr = raw_input("Enter some String: ")

flag = True
for x in strr:
	if(not(ord(x)>=48 and ord(x)<=57)):
		flag = False
		break;
	#end of if
#end of for

if(flag):
	print("String is a Integer Representation")
else:
	print("String is NOT an Integer Representation")
