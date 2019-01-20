from Crypto.Cipher import AES

def pkcs7_pad(string, blocksize=AES.block_size):
	padsize = blocksize - len(string) % blocksize
	if padsize == blocksize:
		return string
	return string + chr(padsize)*padsize

print pkcs7_pad("YELLOW SUBMARINE", blocksize=20)