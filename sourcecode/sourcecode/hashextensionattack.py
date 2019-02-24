# -*- coding: utf8 -*-

import hashlib

def compress(block,
    state=(
        0x67452301,
        0xefcdab89,
        0x98badcfe,
        0x10325476,
        0xc3d2e1f0
    )):
    lrot = lambda x, n: (x << n) | (x >> (32 - n))
    w = []
    for j in range(len(block) // 32):
        w.append(int(block[j * 32: j * 32 + 32], 2))

    for i in range(16, 80):
        w.append(lrot(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1) & 0xffffffff)

    a, b, c, d, e = state

    for i in range(80):
        if i <= 19:
            f, k = d ^ (b & (c ^ d)), 0x5a827999
        elif 20 <= i <= 39:
            f, k = b ^ c ^ d, 0x6ed9eba1
        elif 40 <= i <= 59:
            f, k = (b & c) | (d & (b | c)), 0x8f1bbcdc
        elif 60 <= i <= 79:
            f, k = b ^ c ^ d, 0xca62c1d6

        temp = lrot(a, 5) + f + e + k + w[i] & 0xffffffff
        a, b, c, d, e = temp, a, lrot(b, 30), c, d
    h0 = (state[0] + a) & 0xffffffff
    h1 = (state[1] + b) & 0xffffffff
    h2 = (state[2] + c) & 0xffffffff
    h3 = (state[3] + d) & 0xffffffff
    h4 = (state[4] + e) & 0xffffffff
    return (h0, h1, h2, h3, h4)


def padding(data, blocksize=64):
	leng = "{:0>16}".format(hex(len(data)*8)[2:]).decode("hex")
	return data + '\x80' + (blocksize - len(data) % blocksize - 8 - 1) * '\x00' + leng


# m = hashlib.sha1()
# m.update("secret")
# a = m.hexdigest()
# print a

# padding = '\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000'
# b = 'secret' + padding
# print b.encode("hex")

# c = b + 'append'
# print c.encode("hex")

# padding2 = '\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x020'
# d = c + padding2
# print d.encode("hex")

# msg = 'append\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x020'
# rs1 = 0xe5e9fa1b
# rs2 = 0xa31ecd1a
# rs3 = 0xe84f75ca
# rs4 = 0xaa474f3a
# rs5 = 0x663f05f4

# block = "".join(format(ord(x), '08b') for x in msg)
# r = compress(block, (rs1,rs2,rs3,rs4,rs5))
# print "".join(["%08x" % a for a in r])

# e = hashlib.sha1()
# e.update(c)
# print e.hexdigest()



# secret = 'secret'
# data = 'data'
# append = 'append'
# sig = hashlib.sha1(secret + data).hexdigest()
# print sig

# h = padding(secret+data)
# print h.encode("hex")

# d = padding(secret+data) + append
# print d.encode("hex")
# k = hashlib.sha1(d).hexdigest()
# print k


# a1 = 0x213203cc
# a2 = 0xd63042b2
# a3 = 0x00441a8e
# a4 = 0xf6661641
# a5 = 0x23088ebf

# e = padding(d)[64:]
# print e.encode("hex")

# block = "".join(format(ord(x), '08b') for x in e)

# r = compress(block, (a1,a2,a3,a4,a5))
# print "".join(["%08x" % a for a in r])



# from pwn import *
 
# pwn_socket=ssh(host='challenge02.root-me.org' ,user='app-systeme-ch13' ,password='app-systeme-ch13',port=2222)
# pwned=pwn_socket.process(executable='./ch13')
# pwned.sendline('A' * 40  + '\xef\xbe\xad\xde')
# pwned.sendline('cat .passwd')
# pwned.interactive()

# print hashlib.md5('https://google.com').hexdigest()

f = open("/root/Downloads/dictionary_french.txt").read()
g = open("/root/Downloads/dictionary_french2.txt", "wb")
for i in f:
	g.write(i.upper())

