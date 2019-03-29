import string

something = list('_'*120)
ENCODED = '_'*28
STRING = '_'*28
FINAL = '_'*18
PASSWORD = 'FACEBOOKISEVIL'

k = 0
i = 0
while (i < 5):
	j = 0
	while (j < 5):
		if (k == 9):
			j -= 1
		else:
			something[(6*i+j)*4] = k + 0x41
		k += 1
		j += 1
	i += 1

print something

print PASSWORD

t = 0
length = len(PASSWORD)

for c in range(length):
	for i in range(5):
		for j in range(5):
			if something[(6*i+j)*4] == ord(PASSWORD[c]):
				ENCODED = ENCODED[:t] + chr(ord('A')+i) + ENCODED[t+1:]
				ENCODED = ENCODED[:t+1] + chr(ord('1')+j) + ENCODED[t+2:]
				t += 2

print ENCODED

for c in range(len(ENCODED)):
	STRING = STRING[:c] + chr(ord(ENCODED[c]) ^ (c & 3)) + STRING[c+1:]

print STRING


