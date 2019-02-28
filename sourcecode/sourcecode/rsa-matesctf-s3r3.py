from gmpy2 import *

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


if __name__ == '__main__':
    main()
