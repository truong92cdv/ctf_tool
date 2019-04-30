from random import randint, shuffle
from itertools import permutations


def decrypt(enc, perm):
	W = len(perm)
	msg = ''
	for j in xrange(0, len(enc), W):
		for k in xrange(W):
			msg += enc[j:j+W][perm[k]]

	msg = msg[-1:] + msg[:-1]
	res = ''
	ab = msg[:len(msg)/2]
	cd = msg[len(msg)/2:]
	for i in range(len(msg)/2):
		res += ab[i] + cd[i]
	msg = res
	msg = msg[-1:] + msg[:-1]
	return msg

def checkflag(flag):
	if (flag[:4] == 'ASIS'):
		return True
	return False

def brute():
	for perm in list(permutations(range(W))):
		msg = flag_enc
		print perm
		for l in range(1338):
			msg = decrypt(msg, perm)
			if checkflag(msg):
				print msg
				return

flag_enc = '11d.3ilVk_d3CpIO_4nlS.ncnz3e_0S}M_kn5scpm345n3nSe_u_S{iy__4EYLP_aAAall'
W = 7
brute()






