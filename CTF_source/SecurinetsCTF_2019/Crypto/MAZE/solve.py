from Crypto.PublicKey import RSA
from gmpy2 import *

c = int(open('./chall/cipher.txt', 'r').read())
key1 = RSA.importKey(open('./privatekey1.pem', 'r').read())
key2 = RSA.importKey(open('./privatekey2.pem', 'r').read())

m1 = key1.decrypt(c)
flag1 = hex(m1)[2:-1].decode("hex")
m2 = key2.decrypt(c)
flag2 = hex(m2)[2:-1].decode("hex")
print flag1
print flag2
