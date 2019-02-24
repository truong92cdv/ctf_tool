from Crypto.Cipher import AES

def aes_ecb_decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)

def check_AES_mode_ECB(string):
	if len(string) % 16 != 0:
		return False
	array = [string[i:i+16] for i in range(0, len(string), 16)]
	for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			if array[i] == array[j]:
				return True
	return False

def main():
	lines = [line.rstrip('\n') for line in open('challenge8.txt')]
	for line in lines:
		if check_AES_mode_ECB(line.decode("hex")):
			print(line)

if __name__ == "__main__":
    main()
