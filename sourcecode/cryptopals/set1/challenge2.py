def hex_xor(string1, string2):
    dec1 = int(string1, 16)
    dec2 = int(string2, 16)
    xor = dec1 ^ dec2
    xor_hex = hex(xor)[2:-1]
    if (len(xor_hex) % 2) == 1:
    	xor_hex = '0' + xor_hex
    return xor_hex

def main():
	string1 = '1c0111001f010100061a024b53535009181c'
	string2 = '686974207468652062756c6c277320657965'
	print ("string2: %s" %string2.decode("hex"))
	print hex_xor(string1, string2)	

if __name__ == "__main__":
	main()