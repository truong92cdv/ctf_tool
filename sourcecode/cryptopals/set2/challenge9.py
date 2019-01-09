def pkcs7_pad(string, pad='\x04', blocksize=16):
	return string + pad*(blocksize - len(string) % blocksize)

print pkcs7_pad("YELLOW SUBMARINE", blocksize=20)