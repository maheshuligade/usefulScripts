from math import *
from math import factorial as fact

# def fact(n):
	# return factorial(n)

# Formula for calculating the Combination 
def nCr(n, r):
	return fact(n) // (fact(r) * fact(n - r))

# Formula for calculating the Permutation 
def nPr(n, r):
	return fact(n) // fact(n - r)
