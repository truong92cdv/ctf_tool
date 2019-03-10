#!/usr/bin/python
import gmpy2
from gmpy2 import mpz, isqrt, invert, is_prime
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
	assert(m < isqrt(q/4) and m > 0)
	r = generate_ephemeral_key(q)
	assert(r < isqrt(q/2) and r > 0)
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

def main2():
	f = 148645348470245846308664227698633804822356947203859471772778410040379490471011754394059215850589423477765938112670642488245864652240932955917906518710449098239654028925701100475772690804141652433142428638609841853438972200295070228359624464394495019112494883552123236253512605091982099648990548543384038257745225106432511061786996796185114600975032039928424027903162078771233515540998008729798859837851370687787651348963514610266636767870872075741689975306839634
	g = 35911693977956067049713245458299666622483986017795625594552059041747503464332494915689953716786072346109431238646974060591553381108797202211136626511792605796801093953397162664629799036759806328544457162185469611831186125311784124604904104497675954079524001196994653917183584617214113204299123381218262893478395962961751835141804017822004507668429
	q = 5533948920135635974981004367525470318611791750963759085487158269117125468746685595901701779797085036299260442142061043119789638691555399152381134926986061129682913519371334848512742155446249781557878625885013695635635139321044339748831025349954821142422125824785598989891265148327474570828310315676532878060562970519771267224043613651126800397678231143531028465630066444615738576167758402513546414842004859119350358110811912411812932330177133374303837004558825745492397240781247090411409715820466015091239116566965306157856615340505126470246415875154213380386280501096788700988595097152121184802231971814687613809539965770246455488225052572096195472923401915400685516278543892574816949696098271056676023227815538398708144751963243958803148598499889027009779937905901487767972526189622988094824620224895659171847794116858485588603864293176339191878478690083294544062679397756025346631713076757451644071626766962285771754368377
	priv = PrivateKey(f, g, q)
	priv.export('key.private')
	print decrypt_flag()

if __name__ == '__main__':
	main2()