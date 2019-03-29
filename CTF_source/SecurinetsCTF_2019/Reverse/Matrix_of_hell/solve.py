something = [65, '_', '_', '_', 66, '_', '_', '_', 67, '_', '_', '_', 68, '_', '_', '_', 69, '_', '_', '_', '_', '_', '_', '_', 70, '_', '_', '_', 71, '_', '_', '_', 72, '_', '_', '_', 73, '_', '_', '_', 75, '_', '_', '_', '_', '_', '_', '_', 76, '_', '_', '_', 77, '_', '_', '_', 78, '_', '_', '_', 79, '_', '_', '_', 80, '_', '_', '_', '_', '_', '_', '_', 81, '_', '_', '_', 82, '_', '_', '_', 83, '_', '_', '_', 84, '_', '_', '_', 85, '_', '_', '_', '_', '_', '_', '_', 86, '_', '_', '_', 87, '_', '_', '_', 88, '_', '_', '_', 89, '_', '_', '_', 90, '_', '_', '_', '_', '_', '_', '_']
STRING  = 'B0C2A2C6A3A7C5@6B5F0A4G2B5A2'
ENCODED = '_'*28
PASSWORD = '_'*14

# calculate ENCODED
for c in range(len(STRING)):
	ENCODED = ENCODED[:c] + chr(ord(STRING[c]) ^ (c & 3)) + ENCODED[c+1:]
print ENCODED

# calculate PASSWORD
for c in range(len(PASSWORD)):
	i = ord(ENCODED[c*2]) - ord('A')
	j = ord(ENCODED[c*2+1]) - ord('1')
	PASSWORD = PASSWORD[:c] + chr(something[(6*i+j)*4]) + PASSWORD[c+1:]
print PASSWORD

