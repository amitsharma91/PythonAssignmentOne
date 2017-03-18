"""
Write a Python program to check whether an alphabet is a vowel or consonant
Expected Output
Input a letter of the alphabet k                                       
k is a consonant.
"""

import sys

print("Input a letter of the alphabet: ")
ch = sys.stdin.read(1)

if ch in ('a','e','i','o','u','A','E','I','O','U'):
	sys.stdout.write(str(ch)+" is a vowel")
else:
	sys.stdout.write(str(ch)+" is a consonant")

print("")
