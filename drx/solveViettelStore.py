import subprocess
from telnetlib import *
from random import randint

host,port = '13.251.110.215',10001

# len_secret 8-32
def hash_length_ex(data,len_secret,append,sign,_format):
	res_sign = ''
	res_string = ''
	command = './hash_extender/hash_extender -d "' + data + '" -l ' + str(len_secret) + ' -a "' + append + '" -s "' + sign + '" -f "' + _format + '"'

	p = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	for line in p.stdout.readlines():		
		if line.startswith('New signature:'):
			res_sign = line.split(' ')[2].strip()
		
		if line.startswith('New string:'):
			res_string = line.split(' ')[2].strip()
	
	retval = p.wait()

	return res_sign,res_string

def get():
	r.read_until('4. Exit')
	r.write('2\n')
	r.read_until('Item ID: ')
	r.write('4\n')
	r.read_until('\n')
	data = r.read_until('\n').strip()
	sp = data.rfind('&sign=')
	sign = data[sp+6:]
	data = data[:sp]
	return data,sign

def pay(order):
	r.read_until('4. Exit')
	r.write('3\n')
	r.read_until('Your order: \n')
	r.write(order+'\n')
	r.read_until('\n')
	a = r.read_until('\n')
	if 'FLAG' in a:
		return True
	return False

r = Telnet(host,port)
while True:
	data,sign = get()
	new_sign,new_string = hash_length_ex(data,randint(8,32),'&price=1000&product=FLAG',sign,'sha256')
	new_cre = new_string.decode('hex') + '&sign=' + new_sign
	if pay(new_cre):
		r.interact()
		break

