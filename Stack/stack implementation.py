from stack import Stack

if __name__=="__main__":
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.show()
	stack.pop()
	stack.show()
	print(stack.peek())
	print(stack.count())
	stack.show()