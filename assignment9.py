"""
Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6 
Digits 2
"""

import sys

strr = raw_input("Enter alpha-numeric String: ")

alpha = 0;
numeric = 0;
special = 0

for i in strr:
	if(((ord(i)>=97) and (ord(i)<=122)) or ((ord(i)>=97) and (ord(i)<=122))):
		alpha += 1
	elif((ord(i)>=48) and (ord(i)<=57)):
		numeric += 1
	else:
		special += 1
#end of for

print("Count of Alphabet characters: "+str(alpha))
print("Count of Numbers charachters: "+str(numeric))
print("Count of Special Characters: "+str(special))
