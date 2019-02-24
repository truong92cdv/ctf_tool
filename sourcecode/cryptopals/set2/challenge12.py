import cryptolib, string

secret = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
			aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
			dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
			YnkK""".decode("base64")

def oracle_function(s, key='Vo Nhat TruongTT'):
	return cryptolib.aes_ecb_encrypt(s + secret, key)

alphabet = string.printable

message = ''
hack_dict = {}
stop = False
i = 0
while not(stop):
	print i
	exp = 'A'*(15-i%16)
	# create hack_dict
	for c in alphabet:
		hack_dict[c] = oracle_function(exp + message + c)[:(i//16+1)*16]
	# crack character #i
	s = oracle_function(exp)[:(i//16+1)*16]
	c = '\x00'
	for key, value in hack_dict.items():
		if value == s:
			c = key
	if c == '\x00': 
		stop = True
	else:
		message += c
		print message
		print '-'*80
		i += 1