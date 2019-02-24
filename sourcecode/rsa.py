from Crypto.Util.number import *
from gmpy2 import *


def int_to_bytes(n):
    """Converts the given int n to bytes and returns them."""
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')


def gcd(a, b):
    """Computes the greatest common divisor between a and b using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    """Computes the lowest common multiple between a and b using the GCD method."""
    return a // gcd(a, b) * b


def mod_inv(a, n):
    """Computes the multiplicative inverse of a modulo n using the extended Euclidean algorithm."""
    t, r = 0, n
    new_t, new_r = 1, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t = t + n

    return t


class RSA:
    """Implements the RSA public key encryption / decryption."""

    def __init__(self, key_length, e):
        """In this exercise, e is fixed to 3 so we will have to find p and q that fit the requirements."""
        self.e = e
        phi = 0

        while gcd(self.e, phi) != 1:
            p, q = getPrime(key_length // 2), getPrime(key_length // 2)
            phi = lcm(p - 1, q - 1)
            self.n = p * q

        self._d = mod_inv(self.e, phi)

    def encrypt(self, binary_data):
        """Converts the input bytes to an int (bytes -> int) and then encrypts the int with RSA."""
        int_data = int.from_bytes(binary_data, byteorder='big')
        return pow(int_data, self.e, self.n)

    def decrypt(self, encrypted_int_data):
        """Decrypts the encrypted input data to an int and then converts it back to bytes (int -> bytes)."""
        int_data = pow(encrypted_int_data, self._d, self.n)
        return int_to_bytes(int_data)


def execute(key):
        a = int(iroot(key, 2)[0])
        while 1:
            b2 = a*a - key
            if b2 >= 0:
                b = int(iroot(b2, 2)[0])
                if b*b == b2:
                    break
            a += 1
        p = a+b
        q = a-b
        return p, q

############# CODE SAGE  https://sagecell.sagemath.org/ ################

# err=40
# p2p3=25718339416197155016347059200722990565554067870853545610226371966653516052382546957914320289812433453859436193345068829987610976923180252683267226804850952829 
# p1p4=25718339416197155016347059200722990565554067870853545610226371966653516052380672185338246396962573998431009659213305660299083786739031942533878562393814187971
# p1_approx=isqrt(p1p4/1000000)
# p4_approx=1000000*p1_approx+2**err
# F.<x>=PolynomialRing(Zmod(p1p4),implementation='NTL')
# f=x-p4_approx
# d=f.small_roots(X=2**err,beta=0.5)
# d=d[0]
# p4=p4_approx-d
# p1=int(p1p4)/int(p4)
# p2_approx=isqrt(p2p3/100)
# p3_approx=100*p2_approx+2**err
# F.<x>=PolynomialRing(Zmod(p2p3),implementation='NTL')
# f=x-p3_approx
# d=f.small_roots(X=2**err,beta=0.5)
# d=d[0]
# p3=p3_approx-d
# p2=int(p2p3)/int(p3)
# print('p1',p1)
# print('p2',p2)
# print('p3',p3)
# print('p4',p4)

#########################################################################
def findp(l, u, N):
    p = (l + u) // 2
    i = 100
    p1 = next_prime(p*i)
    p2 = next_prime(p1*i)
    p3 = next_prime(p2*i)
    if p*p1*p2*p3 == N:
        return p, p1, p2, p3
    elif p*p1*p2*p3 > N:
        return findp(l,p,N)
    else:
        return findp(p,u,N)


def main():
    e = 65537
    c = 65730544585056113196855222491649915283458030302678764492256366948316495562844164405260875181381605385931592293174537287502809335112362051614031281550069787125630668940406746065617547709904187617743835592204030473969255847562554773875593313128402311178757607880009338508747805647372484237195480768305231875020498766
    N = 661432982326720220312000264055749897099634058126069682916663983164095399891922239185277584515989571021804685855667350963576552884237075033389449261228025690631313796676189863627781905258968287175185368245091537181600636083142076805504788733126704459028930388517968658736636444935785049391422022025814770038260219959

    i = 100
    l = int(iroot(N/(i**6), 4)[0]) # gmpy2.iroot()
    u = 2 * l
    p, p1, p2, p3 = findp(l,u,N)
    print p, p1, p2, p3, '\n'
    phi = (p-1)*(p1-1)*(p2-1)*(p3-1)
    d = invert(e, phi) # gmpy2.invert()
    m = pow(c, d, N)
    print m, '\n'
    print hex(m)[2:].decode("hex")


def abc():
    n = 2531257
    e = 43
    cipher = [906851, 991083, 1780304, 2380434, 438490, 356019, 921472, 822283, 817856, 556932, 2102538, 2501908, 2211404, 991083, 1562919, 38268]
    p = 509
    q = 4973
    phi = lcm(p-1, q-1)
    d = invert(e, phi)
    message = ''
    for c in cipher:
        m = pow(c, d, n)
        message += str(m)
        

    

if __name__ == '__main__':
    main()