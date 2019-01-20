from random import randint
import cryptolib

def create_random_bytes(length=16):
	return "".join([chr(randint(0,255)) for i in range(length)])

def ecb_cbc_encrypt(data):
	padded_data = create_random_bytes(randint(5,10)) + data + create_random_bytes(randint(5,10))
	key = create_random_bytes()
	if randint(0,1):
		return "ECB", cryptolib.aes_ecb_encrypt(padded_data, key)
	else:
		return "CBC", cryptolib.aes_cbc_encrypt(padded_data, key, create_random_bytes())

data = 'Vo Nhat Truong  Vo Nhat Truong  Vo Vi Khang'
cipher = ecb_cbc_encrypt(data)
print cipher[0]
print cipher[1].encode("hex")
if cryptolib.check_AES_mode_ECB(cipher[1]):
	print "Guess: ECB"
else:
	print "Guess: CBC"