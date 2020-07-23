class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self, head = None):
		self.head = head

	def append(self, new_node):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_node
		else:
			self.head = new_node

	def pop(self):
		current = self.head
		if self.head:
			if self.head.next:
				while current.next.next:
					current = current.next
				current.next = None
			else:
				self.head = None

	def size(self):
		size = 1
		current = self.head
		if self.head:
			while current.next:
				current = current.next
				size += 1
		else:
			size = 0
		return size

	def insert(self, position, new_node):
		current = self.head
		if position <= self.size():
			for i in range(position-2):
				current = current.next
			new_node.next = current.next
			current.next = new_node
		elif position == 1 and self.size() == 0:
			self.head = new_node
		else:
			raise IndexError("Index out of range.")

	def delete(self, position):
		current = self.head
		if position <= self.size():
			for i in range(position-2):
				current = current.next
			current.next = current.next.next
		else:
			raise IndexError("Index out of range")

	def printlist(self):
		print(self.to_array())

	def get_first(self):
		if self.head:
			return self.head.data

	def get_last(self):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			return current.data
		else:
			return None

	def get(self, position):
		current = self.head
		if position<=self.size():
			for i in range(position-1):
				current = current.next
			return current.data
		else:
			raise IndexError("Index out of range")

	def to_array(self):
		array = []
		current = self.head
		for i in range(self.size()):
			array.append(current.data)
			current = current.next
		return array