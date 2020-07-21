class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None

	def printlist(self):
		current = self.head
		if current is not None:
			while current:
				print("{} --> ".format(current.data), end="")
				current = current.next
		else:
			print("Empty List!")




if __name__=="__main__":
	llist = linkedlist()
	llist.head = node(4)
	second = node(5)
	llist.head.next = second
	third = node(6)
	second.next = third
	print(llist.printlist())