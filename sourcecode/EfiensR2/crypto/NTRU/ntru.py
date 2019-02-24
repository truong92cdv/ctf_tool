#!/usr/bin/python
import gmpy
from gmpy import mpz, sqrt, invert, is_prime
import os
from base64 import b64encode, b64decode

######################################################################
# NTRU Crypto System: Public Key and Private Key
# The Private Key contains (f, g, q)
class PrivateKey:
	def __init__(self, f = 0, g = 0, q = 0):
		self.f, self.g, self.q = map(mpz, [f, g, q])
	def export(self, path):
		with open(path, 'w+') as f:
			f.write('\n'.join(map(lambda x: str(x).replace('L', ''), [self.f, self.g, self.q])))
	def read(self, path):
		with open(path, 'r') as f:
			self.f, self.g, self.q = map(int, f.read().split('\n'))

# The Public Key contains (h, q)
class PublicKey:
	def __init__(self, h = 0, q = 0):
		self.h, self.q = map(mpz, [h, q])
	def export(self, path):
		with open(path, 'w+') as f:
			f.write('\n'.join(map(lambda x: str(x).replace('L', ''), [self.h, self.q])))
	def read(self, path):
		with open(path, 'r') as f:
			self.h, self.q = map(int, f.read().split('\n'))
#
######################################################################		
		
######################################################################
# The Key Generation
# Visit https://en.wikipedia.org/wiki/NTRUEncrypt for more information
def generate_key(q_bit_length):
	q = gen_big_prime(q_bit_length)
	while True:
		try:
			f = gen_big_random(q_bit_length/2, msb = 0)
			g = gen_big_random(q_bit_length*3/8)
			assert(f.bit_length() > 0 and f.bit_length() < q_bit_length/2)
			assert(g.bit_length() > q_bit_length/4 and g.bit_length() < q_bit_length/2)
			h = invert(f, q)*g % q
			f_inv = invert(f, g)
			return (PrivateKey(f, g, q), PublicKey(h, q))
		except:
			continue

def gen_big_random(bit_len, msb=1):
	n = (bit_len + 7) / 8
	shift = bit_len % 8 - 1
	if shift < 0: shift = 7
	bit = msb << shift
	mask = (1 << shift) - 1
	s = list(os.urandom(n))
	s[0] = chr((ord(s[0]) & mask) | bit)
	return data_to_int(''.join(s))

def gen_big_prime(bit_len, msb=1):
	while True:
		p = gen_big_random(bit_len, msb)
		if is_prime(p):
			return p
#
######################################################################

def data_to_int(s):
	return mpz(s.encode('hex'), 16)

def int_to_data(e):
	h = hex(e).replace('0x', '').replace('L', '')
	if len(h) % 2:
		h = '0' + h
	return h.decode('hex')

######################################################################
# The NTRU Encryption and Decryption
# Visit https://en.wikipedia.org/wiki/NTRUEncrypt for more information
def encrypt(plaintext, publicKey):
	q, h = map(mpz, [publicKey.q, publicKey.h])
	m = data_to_int(plaintext)
	assert(m < sqrt(q/4) and m > 0)
	r = generate_ephemeral_key(q)
	assert(r < sqrt(q/2) and r > 0)
	e = (r*h + m) % q
	return int_to_data(e)

def decrypt(ciphertext, privateKey):
	q, f, g = map(mpz, [privateKey.q, privateKey.f, privateKey.g])
	f_inv = invert(f, g)
	e = data_to_int(ciphertext)
	a = f*e % q
	b = f_inv*a % g
	return int_to_data(b)

def generate_ephemeral_key(q):
	r = gen_big_random(q.bit_length()/2, msb = 0)
	return r
#
######################################################################

######################################################################
# Flag Encryption and Decryption using NTRU
def encrypt_flag(flag, bit_length=3072):
	# Key Generation
	(privateKey, publicKey) = generate_key(bit_length)
	# Flag Encryption
	C = encrypt(flag, publicKey)
	assert(decrypt(C, privateKey) == flag)
	# Flag Exportation
	publicKey.export('key.public')
	privateKey.export('key.private')
	with open('ciphertext.bin', 'wb+') as f:
		f.write(C)

def decrypt_flag():
	# Private Key Reading
	privateKey = PrivateKey()
	privateKey.read('key.private')
	# Encrypted Flag Reading
	with open('ciphertext.bin', 'rb') as f:
		C = f.read()
	# Flag Decryption
	return decrypt(C, privateKey)
#
######################################################################

def main():
	encrypt_flag('efiens{This_is_not_the_flag_Hi_Hi}')
	print decrypt_flag()

if __name__ == '__main__':
	main()