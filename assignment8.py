"""
Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 
Note :
i = 0,1.., m-1 
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4 
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""
import sys

i = input("Enter Number of Rows: ")
j = input("Enter Number of Columns: ")

sys.stdout.write("[")
for x in range(0,i):
	sys.stdout.write("[")	
	for y in range(0,j):
		sys.stdout.write(str(x*y)+", ")
	#end of inner for
	sys.stdout.write("], ")
#end of outer for
sys.stdout.write("]\n")
