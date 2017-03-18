"""
Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9
"""

import sys


for i in range(1,10):
	for j in range(1,10):
		if(j <= i):
			sys.stdout.write("%d " % i)
		#end of if
	#end of inner for
	print("")
#end of outer for
