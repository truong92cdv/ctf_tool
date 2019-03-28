from gmpy2 import *

def convert(bitstring):
	if bitstring.count('1') >= 3:
		return '1'
	return '0'

p, q, e = 887, 521, 2**16+1
n = p*q
d = invert(e, lcm(p-1, q-1))

f = open('./_ctf_image.png.extracted/output.txt')
data = [line.replace('\r','').replace('\n','').replace('.','') for line in f]
data = [''.join([convert(line[i*5:i*5+5]) for i in range(len(line)/5)]) for line in data]
flag = ''
for bitstring in data:
	flag += hex(pow(int(bitstring, 2), d, n))[2:].decode('hex')
print flag

