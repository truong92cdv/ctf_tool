from pwn import *

p = remote('blind.q.2019.volgactf.ru', 7070)
p.recvline()
p.sendline('1 sign')
command = 'exit'
p.recvline()
p.sendline(command.encode('base64'))
n = p.recvline().strip()
print n
p.recvline()
p.sendline('{} {}'.format(str(n), command))
p.interactive()