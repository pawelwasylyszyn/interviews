#!/usr/bin/python3

def find_primen(limit=100):
	primes = []
	for number in range(1,limit):
		is_prime = 1
		for div in range(2, number):
			if number%div == 0:
				is_prime = 0
		if is_prime == 0:
			continue
		primes.append(number)
	return primes

print(find_primen(100))
