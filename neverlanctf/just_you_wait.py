s = 'jllnunajcxa'
for i in range(26):
	t = ''.join([chr((ord(j)+i) % 26 + 97) for j in s])
	print t

