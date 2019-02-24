from base64 import b64decode
from itertools import combinations
from challenge3 import decrypt_xor, scoring_plaintext
from challenge5 import repeating_key_xor

def hamming_dist(str1, str2):
	return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def stringtobin(string):
	binstring = bin(int(string.encode("hex"), 16))[2:]
	if (len(binstring) % 2 == 1):
		return '0' + binstring
	else:
		return binstring
	# binstring = ''
	# for c in string:
	# 	bin = format(ord(c), 'b')
	# 	bin = '{:0>8}'.format(bin)
	# 	binstring += bin
	# return binstring

def break_repeating_key_xor(binary_data):
	normalized_distances = {}

	for key_size in range(2, 41):
		chunks = [binary_data[i:i + key_size] for i in range(0, len(binary_data), key_size)][:4]
		
		distance = 0
		pairs = combinations(chunks, 2)
		for (x, y) in pairs:
			distance += hamming_dist(stringtobin(x), stringtobin(y))

		distance /= 6
		normalized_distance = distance / key_size
		normalized_distances[key_size] = normalized_distance

	possible_key_sizes = sorted(normalized_distances, key=normalized_distances.get)[:3]
	possible_plaintexts = []

	for d in possible_key_sizes:
		key = ''
		for i in range(d):
			block = ''
			for j in range(i, len(binary_data), d):
				block += binary_data[j]
			key += decrypt_xor(block.encode("hex"))['key']
		possible_plaintexts.append((repeating_key_xor(binary_data, key), key))
	
	return max(possible_plaintexts, key=lambda k: scoring_plaintext(k[0].decode("hex")))

def main():
	with open("challenge6.txt") as f:
		data = b64decode(f.read())

	result = break_repeating_key_xor(data)
	print("Key = " + result[1].decode())
	print("---------------------------------------")
	print(result[0].decode("hex").rstrip())


if __name__ == "__main__":
	main()