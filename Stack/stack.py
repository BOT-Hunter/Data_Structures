class Stack:
	def __init__(self, data=None):
		self.stack = []
		if data:
			self.stack.append(data)

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def clear(self):
		self.stack = []

	def count(self):
		return len(self.stack)

	def to_array(self):
		return self.stack

	def show(self):
		print(self.stack)

