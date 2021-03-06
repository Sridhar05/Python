"""Program to convert decimal to binary"""

# Importing Stack
from stack import Stack

def base_converter(number, base):
	"""Pass"""

	digits = '0123456789ABCDEF'

	# Creating stack object
	s = Stack()	

	while number:
		remainder = number % base
		s.push(str(remainder))
		number /= base

	return s.stack

print base_converter(42, 8)