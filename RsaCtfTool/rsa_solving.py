from Crypto.PublicKey import RSA
from gmpy2 import *
import os

c = open('chall/cipher.txt', 'r').read()
for i in range(47, 100):
	print "Trying {} .................................".format(i)
	command = 'python ./RsaCtfTool.py --publickey chall/pub{0}.pem --private --verbose > chall_1/private{0}.pem'.format(i)
	os.system(command)
	f = open('chall_1/private{0}.pem'.format(i))
	s = f.read()
	f.close()
	print s
	if "BEGIN PRIVATE KEY" in s:
		print "KEY FOUND: ", i
		break

# key = RSA.importKey(open('chall/pub{0}.pem'.format(i), 'r').read())
# n = key.n
# e = key.e
# d = key.d
# p = key.p
# q = key.q

# assert n == p*q
# m = key.decrypt(c)
# flag = hex(m)[2:-1].decode("hex")
# print flag
