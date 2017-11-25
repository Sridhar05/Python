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
		s.push(remainder)
		number /= base

	result = ''
	while not s.is_empty():
		result += digits[s.pop()]

	return result

print base_converter(25, 2)