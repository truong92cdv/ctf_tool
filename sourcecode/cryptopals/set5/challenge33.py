from random import randint

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


A = Diffie_Hellman()
B = Diffie_Hellman()

print A.p
print B.p
print A.g
print B.g
print A.secret_key
print B.secret_key
print A.public_key
print B.public_key
print A.get_shared_key(B.public_key)
print B.get_shared_key(A.public_key)