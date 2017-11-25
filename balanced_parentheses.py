
"""Program to check paranthese is balanced or not"""

# Importing Stack
from stack import Stack

def paranthese_checker(input_string):
	"""pass"""

	# Creating stack object
	s = Stack()	

	balanced = True

	for symbol in input_string:
		if symbol in ['(','{','[']:
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()

	return True if s.is_empty() and balanced else False


print paranthese_checker('[{()]')
	