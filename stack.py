class Stack(object):
	"""Stack Implementation"""

	def __init__(self):
		self.stack = list()
		self.top = -1

	def is_empty(self):
		"""Returns True/False"""
		#return True if self.top == -1 else False
		return self.stack == []

	def peek(self):
		"""Return Top of the stack"""
		return "Top of the stack: {0}".format(self.stack[self.top])

	def push(self, data):
		"""To insert the item to top of the stack"""
		self.top += 1
		self.stack.append(data)
		return "{0} inserted successfully \n {1}".format(data, self.stack)

	def pop(self):
		"""Delete and returns the top element"""
		if self.is_empty():
			return "stack is empty"
		else:
			self.top -= 1
			return "{0} is deleted \n {1}".format(self.stack.pop(), self.stack)

	def size(self):
		"""Return the size of the stack"""
		return "current stack size: {0}".format(len(self.stack))

if __name__ == '__main__':

	obj = Stack()
	print obj.pop()
	print obj.size()
	print obj.push(3)
	print obj.push(True)
	print obj.push(4.5)
	print obj.size()
	print obj.peek()
	print obj.pop()
	print obj.size()