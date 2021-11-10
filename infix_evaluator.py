# Python3 program to evaluate a given
# expression where tokens are
# separated by space.

# Function to find precedence
# of operators.
def precedence(op):
	
	if op == '+' or op == '-':
		return 1
	if op == '*' or op == '/' or op == '%':
		return 2
	if op == '^':
		return 3
	return 0

# Function to perform arithmetic
# operations.
def applyOp(a, b, op):
	
	if op == '+': return a + b
	if op == '-': return a - b
	if op == '*': return a * b
	if op == '/': return a / b
	if op == '%': return a % b
	if op == '^': return a ** b

# Function that returns value of
# expression after evaluation.
def evaluate(tokens):
	
	# stack to store integer values.
	values = []
	
	# stack to store operators.
	ops = []
	i = 0
	
	while i < len(tokens):
		
		# Current token is a whitespace,
		# skip it.
		if tokens[i] == ' ':
			i += 1
			continue
		
		# Current token is an opening
		# brace, push it to 'ops'
		elif tokens[i] == '(':
			ops.append(tokens[i])
		
		# Current token is a number, push
		# it to stack for numbers.
		elif tokens[i].isdigit():
			number = ''
			# There may be more than one
			# digits in the number.
			while (i < len(tokens) and
				(tokens[i].isdigit() or tokens[i] == '.')):
				number += tokens[i]
				i += 1
				
			if number.find('.') == -1:
				val = int(number)
			else:
				number = number.split('.')
				int_val = int(number[0])
				float_val = int(number[1])/(10**len(number[1]))
				val = int_val + float_val
				
			values.append(val)
			
			# right now the i points to
			# the character next to the digit,
			# since the for loop also increases
			# the i, we would skip one
			# token position; we need to
			# decrease the value of i by 1 to
			# correct the offset.
			i-=1
		
		# Closing brace encountered,
		# solve entire brace.
		elif tokens[i] == ')':
		
			while len(ops) != 0 and ops[-1] != '(':
			
				val2 = values.pop()
				val1 = values.pop()
				op = ops.pop()
				
				values.append(applyOp(val1, val2, op))
			
			# pop opening brace.
			ops.pop()
		
		# Current token is an operator.
		else:
		
			# While top of 'ops' has same or
			# greater precedence to current
			# token, which is an operator.
			# Apply operator on top of 'ops'
			# to top two elements in values stack.
			while (len(ops) != 0 and
				precedence(ops[-1]) >=
				precedence(tokens[i])):
						
				val2 = values.pop()
				val1 = values.pop()
				op = ops.pop()
				
				values.append(applyOp(val1, val2, op))
			
			# Push current token to 'ops'.
			ops.append(tokens[i])
		
		i += 1
	
	# Entire expression has been parsed
	# at this point, apply remaining ops
	# to remaining values.
	while len(ops) != 0:
		
		val2 = values.pop()
		val1 = values.pop()
		op = ops.pop()
				
		values.append(applyOp(val1, val2, op))
	
	# Top of 'values' contains result,
	# return it.
	return values[-1]

# Driver Code
if __name__ == "__main__":
	
	exp = input("Enter the infix expression : ")
	val = evaluate(exp)
	if val - int(val) == 0:
		print("result =", int(val))
	else:
		print("reslut =", format(val, '.4f'))

