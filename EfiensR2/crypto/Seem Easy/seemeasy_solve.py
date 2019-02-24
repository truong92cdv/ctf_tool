from gmpy2 import *

def gcd(a, b):
    """Computes the greatest common divisor between a and b using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    """Computes the lowest common multiple between a and b using the GCD method."""
    return a // gcd(a, b) * b


def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls


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


def crt(rp, rq, p, q):
	dp = invert(q, p)
	dq = invert(p, q)
	return (rp*q*dp + rq*p*dq) % (p*q)


n = int(0x1a7cc9f85d483e16040a943b0fbe635f91b6b11a03bc645feeb4d37fcdde2adc7f4ac23f29551334f16a2faf8675977cc9ccfdf981157e32aa2858e28c68354c652d6e93034afcce1288da72928f87e46cb9c585852c954045adbe9dcd5609aff087d6aa7fbb391c6b922b9faef6a1ac2da4ce7eace71641f719049f9227d21d)
c = int(0x16514c70d440c9052e5191c6b6d05880fd6576aaa03711311a5d361195b9ffb791be65f1fc40ddc1aa75d9262bb4589fbf20a914f08ab9d3f6c329345f83bbb1f88522e4a339fb59e65709e536e752430373d8e649e376c09c4646677e7b74db9c463cfa551756ac7baa43a95ef1df25933ac20cf3a01d52545933053b950247)
e = int(0x10006) / 2

p = 4312786190040291036550438673724971590062850705846846309354438515390354238310754941733006083573388386032539416898683338787300084377868976955840648690846001
q = n / p

phi = lcm(p-1, q-1)
d = invert(e, phi)
flag_2 = pow(c, d, n)
print flag_2, '\n'

a = modular_sqrt(flag_2, p)
b = modular_sqrt(flag_2, q)
print a
print b, '\n'

flag = crt(a, b, p, q)
print hex(flag)[2:].decode("hex")


################## CODE SAGE ####################

# n = 0x1a7cc9f85d483e16040a943b0fbe635f91b6b11a03bc645feeb4d37fcdde2adc7f4ac23f29551334f16a2faf8675977cc9ccfdf981157e32aa2858e28c68354c652d6e93034afcce1288da72928f87e46cb9c585852c954045adbe9dcd5609aff087d6aa7fbb391c6b922b9faef6a1ac2da4ce7eace71641f719049f9227d21d
# c = 0x16514c70d440c9052e5191c6b6d05880fd6576aaa03711311a5d361195b9ffb791be65f1fc40ddc1aa75d9262bb4589fbf20a914f08ab9d3f6c329345f83bbb1f88522e4a339fb59e65709e536e752430373d8e649e376c09c4646677e7b74db9c463cfa551756ac7baa43a95ef1df25933ac20cf3a01d52545933053b950247
# e = 0x10006 / 2

# p = 4312786190040291036550438673724971590062850705846846309354438515390354238310754941733006083573388386032539416898683338787300084377868976955840648690846001
# q = n / p

# phi = lcm(p-1, q-1)
# d = inverse_mod(Integer(e), Integer(phi))
# flag_2 = pow(c, d, n)

# a = mod(flag_2, p).sqrt()
# b = mod(flag_2, q).sqrt()
# flag = CRT([Integer(a), Integer(b)], [Integer(p), Integer(q)])

# print format(flag,'x').decode('hex')

#################################################