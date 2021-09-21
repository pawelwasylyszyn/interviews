#!/usr/bin/python3

def fb(x):
	if x%3 == 0:
		if x%5 == 0:
			return "fizzbuzz"
		return "fizz"
	elif x%5 == 0:
		return "buzz"
	else:
		return x

a = [x for x in range(1,31)]
print(list(map(fb,a)))
