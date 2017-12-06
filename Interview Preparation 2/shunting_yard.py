from collections import deque
def is_left_associative():
	pass

def rank():
	return 1

def compare_operator(a, b):
	pass

def get_rid_of_spaces(expression):
	return expression.replace(' ', '')

def check_validity(expression):
	pass

def calculate(expression):
	# Work with clean expression
	expression = get_rid_of_spaces(expression)
	operators, output = [], deque()

	number = ''
	for token in expression:
		# if the token is a digit, append to the digits holder
		if token.isdigit():
			number += token
			continue
		# Its an operator
		else:
			while (operators and rank(operators[-1]) > rank(token)) or (
				rank(operators[-1]) == rank(token) and is_left_associative(operators[-1])) and (
				operators[-1] != '('):



if __name__ == '__main__':
	pass
	# "1 + 1" = 2
	# " 2-1 + 2 " = 3
	# "(1+(4+5+2)-3)+(6+8)" = 23
