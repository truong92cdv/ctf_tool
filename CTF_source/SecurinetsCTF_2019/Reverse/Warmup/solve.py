import string
import itertools

ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits

def pos(char):
	return ALPHABET.index(char)

def func_1(flag):
	v1 = pos(flag[0])
	if (v1 == 0x1c): 						# f[0] = 28 = 'c'
		v1 = pos(flag[0])
		v2 = pos(flag[1])
		v3 = pos(flag[2])
		if (v2 + v1 >> 2) + 1 == v3:		# f[2] = 21 = 'V'
			return 1
	return 0

def func_2(flag):
	v1 = pos(flag[0])
	v2 = pos(flag[1])
	v11 = pos(flag[10])
	return (v2 + v1 >> 2) + 1 == v11		# f[10] = f[2] = 21 = 'V'

def func_3(flag):
	return flag[10] == flag[2] 				# f[10] = f[2] = 21 = 'V'

def func_4(flag):
	return pos(flag[1]) == 0x36 			# f[1] = 54 = '2'

def func_5(flag):
	return flag[3] == 'j'					# f[3] = 'j'

def func_6(flag):
	return ord(flag[0])+1 == ord(flag[4])	# f[4] = 'd'

def func_7(flag):
	arr = [0, 12, 22, 24]
	for i in range(4):
		if ord(flag[arr[i]]) != ord(flag[4])-1:
			return 0
	return 1

def func_8(flag):
	return ord(flag[11])+9 == ord(flag[35])	#

def func_9(flag):
	return ord(flag[3])-0x20 == ord(flag[6])	# f[6] = 'J'

def func_10(flag):
	return (ord(flag[11]) == 0x30) and (ord(flag[23]) == 0x30)	# f[11] = f[23] = '0'

def func_11(flag):
	return ord(flag[0]-1) == ord(flag[8])

def func_12(flag):
	return ord(flag[4])+2 == ord(flag[27]) == ord(flag[31])

def func_13(flag):
	return ord(flag[27])+7 == ord(flag[9]) == ord(flag[25])

def func_14(flag):
	arr = [0xd, 0x11, 0x15]
	for i in range(3):
		if ord(flag[arr[i]]) != ord(flag[1])+1:
			return 0
	return 1

def func_15(flag):
	return flag[7] == 'p'

def func_16(flag):
	return ord(flag[15]) == ord(flag[7])+3

def func_17(flag):
	return ord(flag[15])+1 == ord(flag[14])

def func_18(flag):
	return flag[19] == 'z'

def func_19(flag):
	return ord(flag[0])-33 == ord(flag[34])

def func_20(flag):
	arr = [5, 20, 29, 33]
	result = 0x58
	for i in range(4):
		result = result ^ ord(flag[arr[i]])
	return result == 0x58

def func_21(flag):
	return ord(flag[26]) == 49

def func_22(flag):
	return (ord(flag[9])-32 == ord(flag[16])) and (flag[16] == flag[28])

def func_23(flag):
	return flag[1] == 'c'

def func_24(flag):
	return (ord(flag[7])-30 == ord(flag[18])) and (ord(flag[18]) == ord(flag[30]))

def func_25(flag):
	return flag[32] == flag[4]

f = list('_'*36)
f[0] = 'c'
f[1] = '2'
f[2] = 'V'
f[3] = 'j'
f[4] = 'd'
f[5] = 'X'
f[6] = 'J'
f[7] = 'p'
f[8] = 'b'
f[9] = 'm'
f[10] = 'V'
f[11] = '0'
f[12] = 'c'
f[13] = '3'
f[14] = 't'
f[15] = 's'
f[16] = 'M'
f[17] = '3'
f[18] = 'R'
f[19] = 'z'
f[20] = 'X'
f[21] = '3'
f[22] = 'c'
f[23] = '0'
f[24] = 'c'
f[25] = 'm'
f[26] = '1'
f[27] = 'f'
f[28] = 'M'
f[30] = 'R'
f[31] = 'f'
f[32] = 'd'
f[34] = 'B'
f[35] = '9'

def check(strings):
	ALPHA = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_}{'
	for c in strings:
		if c not in ALPHA:
			return False
	return True

options = itertools.product(ALPHABET, repeat=2)
for i in options:
	if 0x58 ^ ord(f[5]) ^ ord(f[20]) ^ ord(i[0]) ^ ord(i[1]) == 0x58:
		f[29] = i[0]
		f[33] = i[1]
		flag = ''.join(f).decode('base64')
		if check(flag):
			print flag
