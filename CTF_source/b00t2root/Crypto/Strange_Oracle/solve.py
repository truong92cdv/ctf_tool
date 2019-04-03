from pwn import *

DEBUG = False
if DEBUG:
	p = process('oracle.py')
else:
	p = remote('18.188.225.135', 2002)



def encrypt(message):
	p.sendline('1')
	p.sendlineafter('Enter the message: ', message)
	r = p.recvuntil('to do: ').split()[1]
	return r

def decrypt(cipher):
	p.sendline('2')
	p.sendlineafter('Enter the ciphertext: ', cipher)
	r = p.recvuntil('to do: ').split()[1]
	if (r == 'like'):
		return 0
	else:
		return 1

p.sendlineafter('to do: ', '3')
flag_enc = p.recvuntil('to do: ').split()[0]
print flag_enc

upper_limit = N
lower_limit = 0
flag = ""
i = 1

while i <= 1024:
	# c = encrypt(hex(2)[2:].decode('hex'))
	chosen_ct = 
    output = decrypt(chosen_ct)
    if output == 0:
        upper_limit = (upper_limit + lower_limit)/2
    elif output == 1:
        lower_limit = (lower_limit + upper_limit)/2
    else:
        throw Exception
    i += 1

flag = 

# a = encrypt('drx')
# print a
# b = decrypt(a)
# print b
