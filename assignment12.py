"""
 
"""
import sys

months = ["January", "February","March","April","May","June","July","August","September","October","November","December"]

for m in months:
	sys.stdout.write(str(m)+" , ")

mon = raw_input("\nEnter the Month Name as above: ")

if mon in months:
	if months.index(mon) in (0,2,4,6,7,9,11):
		print("No. of Days: 31 days")
	elif months.index(mon) in (3,5,8,10):
		print("No. of Days: 30 days")
	elif(months.index(mon) == 1):
		print("No. od Days: 28/29")
else:
	print("Invlid Months Name.")
