from Crypto.PublicKey import RSA
from gmpy2 import *

c = int(open('./chall/cipher.txt', 'r').read())
keys = [RSA.importKey(open('./chall/pub{}.pem'.format(i), 'r').read()) for i in range(101)]
for i in range(101):
	for j in range(i+1, 101):
		factor = gcd(keys[i].n, keys[j].n)
		if factor != 1:
			assert keys[i].e == keys[j].e
			e = keys[i].e
			p = factor
			n1 = keys[i].n
			n2 = keys[i].n
			break
			
if (p != 1):
	q1 = n1/p
	q2 = n2/p
	phi1 = lcm(p-1, q1-1)
	phi2 = lcm(p-1, q2-1)
	d1 = invert(e, phi1)
	d2 = invert(e, phi2)
	m1 = pow(c, d1, n1)
	m2 = pow(c, d2, n2)
	flag1 = hex(m1)[2:].decode("hex")
	flag2 = hex(m2)[2:].decode("hex")
	print 'PRIVATE KEY FOUND: ...\n\nCOMMON FACTOR: p = {}\n'.format(p)
	print 'flag1: ', flag1
	print 'flag2: ', flag2