import os,random,sys,string
from hashlib import sha256
import CompactFIPS202

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


def findsecret():
	sponge = 'fwWeu3dkM8Lg9g0G'
	digest = '334987856e6d434349c834ee8b005da3ad968d3c196b6bbec0b24536d3529597'
	LETTERS = string.ascii_letters+string.digits
	print LETTERS	

	secret = LETTERS[0]*4
	while (1):
		print 'Trying ... ', secret
		if secret==False:
			print 'Finish'
			break
		hashed = sha256(secret + sponge).hexdigest()
		if hashed==digest:
			print 'secret: ...............', secret
			break
		secret = next(secret, LETTERS)
	return secret


def dohash(msg):
	return CompactFIPS202.Keccak(1552, 48, bytearray(msg), 0x06, 32)

# secret = findsecret()
secret = 'mhgi'
message = 'drxiscomingasldjf;lasdjflas'

m1 = """FECA67BD2D3F021A|BD10A64A4C2B774F|F8EF6FF82DD21FC7|6F4BA4D964A78764|0F4FD1C92A24BC6E
FB4B8C0A11C64088|EDA7B9EBC05F50A8|0A71DD08E7F1EB5B|5342D2AE78A8BFB5|6591A9B0CC2E7CE9
52A3DD827F4EF6DC|9D89B18362B80DE4|FEA719A1875BFFF7|49A2B95AD7B7D147|B23784B72EB9260A
187AEFD07295FD59|EE806366EF9D09FF|0000000000000000|0000000000000000|0000000000000000
0000000000000000|0000000000000000|0000000000000000|0000000000000000|0000000000000000"""
m1 = m1.replace('|', '').replace('\n','')
m1 = m1.decode("hex")

m2 = """16F97050842C2D17|A731EE935A43480A|6D8E356BDBD7CBE9|D62C0B356FFA158A|4FAD968080C7F8C8
7C83B8E1C61BC5AB|7E3FCA22B5E29305|5888D4DBE848C840|236DE21CCEF77B8A|69D59EF589070E60
E87FCD2BF2C6CCE1|B1E28B821FD93ABC|AD5D6FB1860CB45C|AB8FC7D1015975D5|24C6B737EE96CC23
D3BFB5957965A447|EE31D3F5269F254F|0000000000000000|0000000000000000|0000000000000000
0000000000000000|0000000000000000|0000000000000000|0000000000000000|0000000000000000"""
m2 = m2.replace('|', '').replace('\n','')
m2 = m2.decode("hex")

# assert dohash(m1)==dohash(m2)
print dohash(message)