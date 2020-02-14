def add(*args):
	sum = 0
	for arg in args:
		sum += arg
	return sum
print(add(1,2))
print(add(-1,-1))
print(add(1,2,3,4,5))

def multiply(*args):
	product = 1
	for arg in args:
		product *= arg
	return product
print(multiply(1,3))
print(multiply(-1,3))
print(multiply(1,2,3,4,5))