import os, subprocess
from random import randint

payment = "product=Itel A32F&price=1350000&timestamp=1550422661239732&sign=0235ee99263b53470fd75c9b60a736baab024746698809f453ccf82247a39cf4"

sp = payment.rfind('&sign=')
sign = payment[sp+6:]
data = payment[:sp]
append = "&product=FLAG&price=1000"
_format = "sha256"

def hash_length_ex(data,len_secret,append,sign,_format):
	res_sign = ''
	res_string = ''
	command = '~/ctf_tool/hash_extender/hash_extender -d "' + data + '" -l ' + str(len_secret) + ' -a "' + append + '" -s "' + sign + '" -f "' + _format + '"'

	p = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	for line in p.stdout.readlines():		
		if line.startswith('New signature:'):
			res_sign = line.split(' ')[2].strip()
		
		if line.startswith('New string:'):
			res_string = line.split(' ')[2].strip()
	
	retval = p.wait()

	return res_sign,res_string

for len_secret in range(8,33):
	new_sign,new_string = hash_length_ex(data,randint(8,32),'&price=1000&product=FLAG',sign,'sha256')
	new_cre = new_string.decode('hex') + '&sign=' + new_sign
	print len_secret
	print new_cre
	print