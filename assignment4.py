"""
Write a Python program that accepts a word from the user and reverse it.
"""

import sys

"""
print("Enter some String: ")
strr = sys.stdin.readline()
"""

strr = raw_input("Enter some String: ")

i = len(strr)-1;

sys.stdout.write("Reverse of a String is: ")
while(i>=0):
	sys.stdout.write(strr[i])
	i-=1
#end of while
print("")

"""
for i in strr:
	print(i+" => "+str(ord(i)))
"""
