import challenge3

def main():
	f = open("challenge4.txt").readlines()
	array = [x.strip() for x in f]

	decrypt_array = []
	for s in array:
		decrypt_array.append(challenge3.decrypt_xor(s))

	result = decrypt_array[0]
	for r in decrypt_array:
		if r['score'] > result['score']:
			result = r

	print(result['plaintext'] + "\nScore: " + "{0:.2f}\n".format(result['score']))


if __name__ == "__main__":
	main()