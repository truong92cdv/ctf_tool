import os,random,sys,string
from hashlib import sha256

def next(secret, LETTERS):
	i = len(secret) - 1
	while (1):
		if secret[i] != LETTERS[-1]:
			index = i
			break
		i -= 1
		if (i == -1):
			index = -1
			break
	if (index==-1):
		return False
	else:
		return secret[:index] + LETTERS[LETTERS.find(secret[index])+1] + LETTERS[0]*(len(secret)-1-index)


def findsecret(sponge, digest, LETTERS):
	print 'Trying to find secret 2 ...'
	secret = LETTERS[0]*4
	while (1):
		if secret[1:] == '000':
			print 'Trying {}___'.format(secret[0])
		if secret==False:
			print 'Finish'
			break
		hashed = sha256(secret + sponge).hexdigest()
		if hashed==digest:
			print 'secret: ', secret
			break
		secret = next(secret, LETTERS)
	return secret


# m1 = """FECA67BD2D3F021A|BD10A64A4C2B774F|F8EF6FF82DD21FC7|6F4BA4D964A78764|0F4FD1C92A24BC6E
# FB4B8C0A11C64088|EDA7B9EBC05F50A8|0A71DD08E7F1EB5B|5342D2AE78A8BFB5|6591A9B0CC2E7CE9
# 52A3DD827F4EF6DC|9D89B18362B80DE4|FEA719A1875BFFF7|49A2B95AD7B7D147|B23784B72EB9260A
# 187AEFD07295FD59|EE806366EF9D09FF|0000000000000000|0000000000000000|0000000000000000
# 0000000000000000|0000000000000000|0000000000000000|0000000000000000|0000000000000000"""
# m1 = m1.replace('|', '').replace('\n','')
# m1 = m1.decode("hex")

# m2 = """16F97050842C2D17|A731EE935A43480A|6D8E356BDBD7CBE9|D62C0B356FFA158A|4FAD968080C7F8C8
# 7C83B8E1C61BC5AB|7E3FCA22B5E29305|5888D4DBE848C840|236DE21CCEF77B8A|69D59EF589070E60
# E87FCD2BF2C6CCE1|B1E28B821FD93ABC|AD5D6FB1860CB45C|AB8FC7D1015975D5|24C6B737EE96CC23
# D3BFB5957965A447|EE31D3F5269F254F|0000000000000000|0000000000000000|0000000000000000
# 0000000000000000|0000000000000000|0000000000000000|0000000000000000|0000000000000000"""
# m2 = m2.replace('|', '').replace('\n','')
# m2 = m2.decode("hex")

sponge = '{T7Em`dix?Y#G8(;'
digest = '0a532b54c5043e57a2dba2cdd8b2863951cab135e7a2158c325716e8f4810664'
LETTERS = string.printable
# secret1 = findsecret(sponge, digest, LETTERS)
secret1 = 'bbS`'

sponge = 'j|:!_LO_[Lg32P5c'
digest = '723d4aba2b2d51619aa8e58dfc801a6cc0fb2a35ce53529c5905601d70c86f9e'
LETTERS = string.printable
# secret2 = findsecret(sponge, digest, LETTERS)
secret2 = 'C(FL'


PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
i = 1
print PC_1[i:] + PC_1[:i]

