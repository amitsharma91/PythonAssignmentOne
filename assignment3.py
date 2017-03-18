"""
Write a Python program to construct the following pattern, using a nested for loop.
	*	
	* *
	* * *
	* * * *
	* * * * *
	* * * *
	* * *
	* *
	*
"""
import sys

flag = 0;
k=1;
i=1
while(i<6):
	j=1
	while(j<6):
		if(j<=k):
			sys.stdout.write("* ")
		j+=1;
	#end of inner while
	i+=1;	
	if(k==5):
		flag = 1;
		i = 1;

	if(flag == 0):
		k+=1;

	if(flag == 1):
		k-=1;
	print("")	
#end of outer while





