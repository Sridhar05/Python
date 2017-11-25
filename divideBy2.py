"""Program to convert decimal to binary"""

# Importing Stack
from stack import Stack

def divide_by_two(number):
	"""Pass"""

	# Creating stack object
	s = Stack()	

	while number:
		remainder = number % 2
		s.push(str(remainder))
		number /= 2

	return ''.join(s.stack)[::-1]

print divide_by_two(42)