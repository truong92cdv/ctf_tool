import base64, string
from itertools import combinations

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
    return "".join([alpha[(alpha.find(c) + key) % len(alpha)] for c in string])


