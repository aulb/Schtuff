#!/usr/bin/env python
# Reverse Polish Notation
# https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def evaluate(i1, i2, notation):
	if notation == "+":
		return i1 + i2
	elif notation == "-":
		return i1 - i2
	elif notation == "*":
		return i1 * i2
	elif notation == "/":
		return i1 / i2
	else:
		raise "Notation invalid."
	# Division by 0 error too


def reverse_polish_notation(A):
	number_stack = Stack()
	length = len(A)
	for i in range(length):
		if type(A[i]) == int:
			number_stack.push(A[i])
		else:
			try:
				a = number_stack.pop()
				b = number_stack.pop()
				number_stack.push(evaluate(a, b, A[i]))
			except:
				raise Exception("Not a valid Polish notation.")

	return number_stack.pop()

if __name__ == '__main__':
	print reverse_polish_notation([1,2,3,0,"+", "-"])
