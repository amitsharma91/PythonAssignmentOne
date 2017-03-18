"""
Write a python program to find those numbers which are divisible by 7 and multiple by 5, between 1500 and 2700(both included.)

"""
import sys

print("Numbers multiple of 5 and Divisible by 7 are: ")
for i in range(1500,2701):
	if(i%7==0 and i%5==0):
		sys.stdout.write(str(i)+" ")
	#end of if
#end of for
print("")
