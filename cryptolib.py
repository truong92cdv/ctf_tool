import base64, string
from random import randint
from itertools import combinations
from Crypto.Cipher import AES


class Diffie_Hellman():

	default_p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b225'
                    '14a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f4'
                    '4c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc20'
                    '07cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed5'
                    '29077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff', 16)
	default_g = 2

	def __init__(self, p=default_p, g=default_g):
		self.p = p
		self.g = g
		self.secret_key = randint(0, p-1)
		self.public_key = pow(g, self.secret_key, p)
		self.shared_key = None

	def get_shared_key(self, partner_public_key):
		if self.shared_key is None:
			self.shared_key = pow(partner_public_key, self.secret_key, self.p)
		return self.shared_key

# input  = 	'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# output =	'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
def hex_to_base64(string):
	return base64.b64encode(string.decode("hex"))

# input1 = '1c0111001f010100061a024b53535009181c'
# input2 = '686974207468652062756c6c277320657965'
# output = '746865206b696420646f6e277420706c6179'
def hex_xor(string1, string2):
    xor_hex = hex(int(string1, 16) ^ int(string2, 16))[2:-1]
    if (len(xor_hex) % 2) == 1:
    	xor_hex = '0' + xor_hex
    return xor_hex

def string_xor(str1, str2):
	return "".join([chr(ord(x) ^ ord(y)) for x, y in zip(str1, str2)])

# string = 'Cooking MC's like a pound of bacon'
# score  = 2.2641049
def scoring_plaintext(string):
	standard_frq = {
		'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    	'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    	'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    	'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
	}

	string = string.lower()
	score = 0
	for char in string:
		if char in standard_frq.keys():
			score += standard_frq[char]
	return score

# string = '77316?x+x413=x9x(7-6<x7>x:9;76'
# output = {'plaintext': "Cooking MC's like a pound of bacon", 'score': 2.2641049, 'key': 'X'}
def decrypt_xor(string):
	string = string.encode("hex")
	result_array = []
	for i in range(32, 127):
		keystring = (chr(i)*(len(string)/2)).encode("hex")
		plaintext = hex_xor(string, keystring).decode("hex")
		result = {
			'key': chr(i),
			'score': scoring_plaintext(plaintext),
			'plaintext': plaintext
		}
		result_array.append(result)

	sorted_result = sorted(result_array, key=lambda c: c['score'], reverse=True)[0]
	return sorted_result

# string = "Burning 'em, if you ain't quick and nimble\tI go crazy when I hear a cymbal"
# key 	 = "ICE"
# output = "67'*+.cb,.ii*#i:*<c$ -b=c4<*&"c$''e'*(+/ @ \ne.,e*1$3:e>+ 'ci+ (1e(c&0.'(/"
def repeating_key_xor(string, key):
	keystring = ""
	for i in range(len(string)):
		keystring += key[i % len(key)]
	result = hex_xor(string.encode("hex"), keystring.encode("hex")).decode("hex")
	return result

# str1   = 'Hello world!'
# str2 	 = 'hello robert'
# output = 6
def hamming_dist(str1, str2):
	return sum(c1 != c2 for c1, c2 in zip(str1, str2))

# string = 'Hello world!'
# output = '010010000110010101101100011011000110111100100000011101110110111101110010011011000110010000100001'
def stringtobin(string):
	binstring = bin(int(string.encode("hex"), 16))[2:]
	res = len(binstring) % 8
	return '0'*(8-res) + binstring

# binary_data = 
# output  	  = (message, key)
def break_repeating_key_xor(data, max_keysize=20):
	normalized_distances = {}

	for key_size in range(2, max_keysize):
		chunks = [data[i:i + key_size] for i in range(0, len(data), key_size)][:4]
		
		distance = 0
		pairs = combinations(chunks, 2)
		for (x, y) in pairs:
			distance += hamming_dist(x, y)

		distance /= 6.0
		normalized_distance = distance / key_size
		normalized_distances[key_size] = normalized_distance

	possible_key_sizes = sorted(normalized_distances, key=normalized_distances.get)[:5]
	print possible_key_sizes
	possible_plaintexts = []

	for d in possible_key_sizes:
		key = ''
		for i in range(d):
			block = ''
			for j in range(i, len(data), d):
				block += data[j]
			key += decrypt_xor(block)['key']
		possible_plaintexts.append((repeating_key_xor(data, key), key))
	
	return max(possible_plaintexts, key=lambda k: scoring_plaintext(k[0]))

# string = 'Hello world!!!!!kdiasoiughjkioklHello world!!!!!lkjkdjghklapopsdHello world!!!!!'
# output = True
def check_AES_mode_ECB(string):
	if len(string) % 16 != 0:
		return False
	array = [string[i:i+16] for i in range(0, len(string), 16)]
	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			if array[i] == array[j]:
				return True
	return False

# string = 'RHNTKXTMTEXGMXWWXVMBOX'
# key    = 7
# alpha  = string.ascii_uppercase
# output = 'YOUAREATALENTEDDECTIVE'
def sub_cipher(string, key, alpha):
	m = ''
	for c in string:
		index = alpha.find(c)
		if index >= 0:
			m += alpha[(index + key) % len(alpha)]
		else:
			m += c
	return m
    # return "".join([alpha[(alpha.find(c) + key) % len(alpha)] for c in string])

# string = 'Vo Nhat Truong'
# output = 'Vo Nhat Truong'
def pkcs7_pad(string, blocksize=AES.block_size):
	padsize = blocksize - len(string) % blocksize
	if padsize == blocksize:
		return string
	return string + chr(padsize)*padsize

# reverse of pkcs7_pad
def pkcs7_unpad(string, blocksize=AES.block_size):
	pad_num = ord(string[-1])
	if (pad_num > 0) and (pad_num < 16):
		return string[:-pad_num]
	return string

# string = 'Vo Nhat Truong'
# output.encode("hex") = 'a958e7debc8b678d4251847123df792e'
def aes_ecb_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pkcs7_pad(data))

# reverse of aes_ecb_encrypt()    
def aes_ecb_decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)

def _aes_cbc_encrypt(data, key, iv):
	data = pkcs7_pad(data)
	ciphertext = ''
	prev = iv
	for i in range(0, len(data), AES.block_size):
		prev = aes_ecb_encrypt(string_xor(data[i:i+AES.block_size], prev), key)
		ciphertext += prev
	return ciphertext

def _aes_cbc_decrypt(data, key, iv):
	plaintext = ''
	prev = iv
	for i in range(0, len(data), AES.block_size):
		prev = string_xor(aes_ecb_decrypt(data[i:i+AES.block_size], key), prev)
		plaintext += prev
	return plaintext

# encrypt data with mode CBC
def aes_cbc_encrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pkcs7_pad(data))

# decrypt data with mode CBC
def aes_cbc_decrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return pkcs7_unpad(cipher.decrypt(data))

# create a string of radom bytes with given length
def create_random_bytes(length=16):
	return "".join([chr(randint(0,255)) for i in range(length)])

# Return Substitution Cipher with Mode 'ENCRYPT' or 'DECRYPT'
def substitution_cipher(message, MODE, key):
    
    translated = ''
    charsA = LETTERS
    charsB = key
    
    if MODE.upper() == 'DECRYPT':
        charsA, charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated


# m = 'Trying to decrypt something else to see if it works.jjjjjjjjjjjj'
# k = 'Vo Nhat Truong88'
# iv = '\x00' * AES.block_size
# c = aes_cbc_encrypt(m, k, iv)
# d = aes_cbc_decrypt(c, k, iv)
# print len(c)
# print len(m)
# print len(d)
# print d

# A = Diffie_Hellman()
# B = Diffie_Hellman()

# print A.p
# print B.p
# print A.g
# print B.g
# print A.secret_key
# print B.secret_key
# print A.public_key
# print B.public_key
# print A.get_shared_key(B.public_key)
# print B.get_shared_key(A.public_key)