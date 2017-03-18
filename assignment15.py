"""
	Write a Python program to check a triangle is equilateral, isosceles or scalene.
	Note :
	An equilateral triangle is a triangle in which all three sides are equal.
	A scalene triangle is a triangle that has three unequal sides.
	An isosceles triangle is a triangle with (at least) two equal sides.
	Expected Output:
	Input lengths of the triangle sides:                                    
	x: 6                                                                    
	y: 8                                                                    
	z: 12                                                                   
	Scalene triangle 
"""

print("Input lengths of the triangle sides:")
x = input("x: ")
y = input("y: ")
z = input("z: ")

if(x == y == z):
	print("Triangle is an Equilateral Triangle")
if(x != y and x != z and y != z):
	print("Triangle is an Scalene Triangle")
if((x == y != z) or (x == z != y) or (y == z != x)):
	print("Triangle is an Isosceles Triangle")
