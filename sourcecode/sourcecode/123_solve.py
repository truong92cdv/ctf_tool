from pwn import *

def chose(cpt_left, cpt_right, left, right):
	if ((cpt_left == 1) and (cpt_right == 1)):
		return 'L' # Bua > Keo
	if (((cpt_left == 1) and (cpt_right == 2)) or ((cpt_left == 2) and (cpt_right == 1))):
		return 'L' # Bua > Keo or Bua = Bua
	if (((cpt_left == 1) and (cpt_right == 3)) or ((cpt_left == 3) and (cpt_right == 1))):
		return 'L' # Bua > Keo or Bua < Bao
	if ((cpt_left == 2) and (cpt_right == 2)):
		return 'R' # Bua > Keo
	if (((cpt_left == 2) and (cpt_right == 3)) or ((cpt_left == 3) and (cpt_right == 2))):
		return 'R'
	if ((cpt_left == 3) and (cpt_right == 3)):
		return 'R'

CHOICE = {'0': 0, 'Keo': 1, 'Bua': 2, 'Bao': 3}
score = 15

p = remote(host='192.168.1.6', port=2224)
p.sendline('drx')
p.sendlineafter('Please select: ','2')
p.sendlineafter('...!','a')
while (True):
	p.recvuntil('left hand: ')
	p.sendline('2')
	p.recvuntil('right hand: ')
	p.sendline('3')
	select = p.recvuntil('Please select: ')
	f = open('123.txt','w')
	f.write(select.strip())
	print select.strip().split()
	cpt_left  = int(CHOICE[select.strip().split()[23]])
	cpt_right  = int(CHOICE[select.strip().split()[26]])
	left = 2
	right = 3
	f.write('{} {}\n'.format(left, right))
	f.write('{} {}\n'.format(cpt_left, cpt_right))
	
	c = chose(cpt_left, cpt_right, left, right)
	f.write('You chose: {}\n'.format(c))
	p.sendline(c)
	r = p.recv(1024)
	f.write(r)
	p.sendline()
	r = p.recv(1024)
	f.write(r)
	p.sendline()
	r = p.recv(1024)
	f.write(r.strip())
	score = r.strip().split()[:-1]
	print 'score: {}\n'.format(score)
	f.write('score: {}'.format(score))
	f.close()
	p.sendline('y')
p.interactive()