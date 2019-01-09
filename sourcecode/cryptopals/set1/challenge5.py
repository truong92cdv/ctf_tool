import challenge2
import base64

def repeating_key_xor(string, key):
	keystring = ""
	for i in range(len(string)):
		keystring += key[i % len(key)]
	result = challenge2.hex_xor(string.encode("hex"), keystring.encode("hex"))
	return result


def main():
	string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	key = "ICE"
	print repeating_key_xor(string, key)

if __name__ == "__main__":
	main()
