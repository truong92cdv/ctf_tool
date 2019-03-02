from gmpy2 import *

def crt(Remainders, Modules):
	assert len(Remainders) == len(Modules)
	n = len(Modules) # number of modules

	# M = m1*m2*...*mn
	M = 1  
	for m in Modules:
		M *= m

	# M[i] = M / m[i]
	M_array = []
	for i in range(n):
		M_array.append(M / Modules[i])

	# y[i] = (M[i]^-1) mod m1
	y_array = []
	for i in range(n):
		y_array.append(invert(M_array[i], Modules[i]))
	
	Result = 0
	for i in range(n):
		Result += Remainders[i] * M_array[i] * y_array[i]
	
	return Result % M


Remainders = (2, 3, 5)
Modules = (3, 5, 7)
print crt(Remainders, Modules)