"""
Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish
"""

sum = 0;
cnt = 0
while(True):
	num = input("Enter Number: ")
	if(num == 0):
		break
	sum += num
	cnt += 1
#end of while

print("Sum of Numbers is: "+str(sum))
print("Average of Numbers is: %f" % (float(sum) / float(cnt)))
