from random import randint
import hashlib
import cryptolib

class Diffie_Hellman():

	default_p = int('ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b225'
                    '14a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f4'
                    '4c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc20'
                    '07cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed5'
                    '29077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff', 16)
	default_g = 2

	def __init__(self, p=default_p, g=default_g):
		self.p = p
		self.g = g
		self.secret_key = randint(0, p-1)
		self.public_key = pow(g, self.secret_key, p)
		self.shared_key = None

	def get_shared_key(self, partner_public_key):
		if self.shared_key is None:
			self.shared_key = pow(partner_public_key, self.secret_key, self.p)
		return self.shared_key

msg = "Vo Nhat Truong Vo Vi Khang 01/05/1992"
print "msg:              %s\n" % msg

Alice = Diffie_Hellman()
# Alice -> Eve: 	Send p,g,A
A = Alice.public_key
p = Alice.p
g = Alice.g
Eve   = Diffie_Hellman(p, g)
# Eve   -> Bob:		Send p,q,p
E = Eve.p
Bob   = Diffie_Hellman(p, g)
# Bob   -> Eve: 	Send B
B = Bob.public_key
# Eve   -> Alice: send p


# Alice -> Eve:		Send AES-CBC(SHA1(s)[0:16], iv=random(16), msg) + iv
iv = cryptolib.create_random_bytes()
cipher = hashlib.sha1()
cipher.update(str(Alice.get_shared_key(E)))
encrypted_msg_1 = cryptolib.aes_cbc_encrypt(msg, cipher.digest()[:16], iv)
print "Alice -> Eve:     %s\n" % encrypted_msg_1.encode("hex")


# Eve decrypt to find msg
s = 0
cipher = hashlib.sha1()
cipher.update(str(s))
decrypted_msg_1 = cryptolib.aes_cbc_decrypt(encrypted_msg_1, cipher.digest()[:16], iv)
print "Eve find the msg: %s\n" % decrypted_msg_1


# Eve replay that to Bob.
encrypted_msg_2 = cryptolib.aes_cbc_encrypt(decrypted_msg_1, cipher.digest()[:16], iv)
print "Eve   -> Bob:     %s\n" % encrypted_msg_2.encode("hex")


# Bob decrypt to find msg
cipher = hashlib.sha1()
cipher.update(str(Bob.get_shared_key(E)))
decrypted_msg_2 = cryptolib.aes_cbc_decrypt(encrypted_msg_2, cipher.digest()[:16], iv)
print "Bob find the msg: %s\n" % decrypted_msg_2
# Bob   -> Eve:		Send AES-CBC(SHA1(s)[0:16], iv=random(16), A's msg) + iv
encrypted_msg_3  = cryptolib.aes_cbc_encrypt(decrypted_msg_2, cipher.digest()[:16], iv)
print "Bob   -> Eve:     %s\n" % encrypted_msg_3.encode("hex")


# Eve replay that to Alice
# cipher.update(str(s))
decrypted_msg_3 = cryptolib.aes_cbc_decrypt(encrypted_msg_3, cipher.digest()[:16], iv)
encrypted_msg_4 = cryptolib.aes_cbc_encrypt(decrypted_msg_3, cipher.digest()[:16], iv)
print "Eve -> Alice:     %s\n" % encrypted_msg_4.encode("hex")
