import challenge2

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


def decrypt_xor(string):
	result_array = []
	for i in range(32, 127):
		keystring = (chr(i)*(len(string)/2)).encode("hex")
		plaintext = challenge2.hex_xor(string, keystring).decode("hex")
		result = {
			'key': chr(i),
			'score': scoring_plaintext(plaintext),
			'plaintext': plaintext
		}
		result_array.append(result)

	sorted_result = sorted(result_array, key=lambda c: c['score'], reverse=True)[0]
	return sorted_result


def main():
	string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	result = decrypt_xor(string)
	print(result['plaintext'] + "\nScore: " + "{0:.2f}\n".format(result['score']))

if __name__ == "__main__":
	main()
