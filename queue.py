"""Queue implementation using python"""

class Queue(object):

	def __init__(self):
		self.queue = list()

	def enqueue(self, item):
		self.queue.insert(0, item)


	def dequeue(self):
		self.queue.pop()

	def is_empty(self):
		return self.queue == []

	def size(self):
		return len(self.queue)

if __name__ == '__main__':
	q = Queue()
	print q.is_empty()
	q.enqueue(10)
	q.enqueue(11)
	q.enqueue(12)
	q.enqueue(13)
	q.enqueue(14)
	q.dequeue()
	print q.queue