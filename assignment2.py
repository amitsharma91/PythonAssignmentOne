"""
Write a Python program to convert temperatures to and from celsius, fahrenheit. 
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
Expected Output : 
60C is 140 in Fahrenheit
45F is 7 in Celsius
"""

import sys

#fahrenheit to Celsius
def faren_to_cels(temp):
	conv = ((temp-32)*5)/9;
	return conv
#edn of faren_to_cels()

#Celcius to Farenheit
def cels_to_faren(temp):
	conv = ((temp*9)/5)+32
	return conv 
#end of fcels_to_faren()

ch = input("Select an Operation: \n1.) Farenheit to Celsius\n2.) Celsius to Farenheit\nYour choice:  ")
if(ch == 1):
	t = input("Enter Temperature in Farenheit: ")
	print(str(t)+" F -> "+str(faren_to_cels(t))+" C")
if(ch == 2):
	t = input("Enter Temperature in Celsius: ")
	print(str(t)+" C -> "+str(cels_to_faren(t))+" F")
else:
	print("Invalid Choice")
print("")
