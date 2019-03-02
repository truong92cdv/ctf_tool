from gmpy2 import *

n = 1249110767794010895540410194153
e = 65537
d = 205119704640110252892051812353

e_VICTIM = 3

k = (e*d-1)/n

while True:
	phi = (e*d-1)/k
	if phi*k == (e*d-1):
		break
	k += 1

d_VICTIM = invert(e_VICTIM, phi)
print 'phi =', phi
print 'd_VICTIM =', d_VICTIM