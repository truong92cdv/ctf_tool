import sys
from sympy.solvers import solve
from sympy import Symbol

# A reimplementation of pablocelayes rsa-wiener-attack for this purpose
# https://github.com/pablocelayes/rsa-wiener-attack/


class WienerAttack(object):
    def rational_to_contfrac(self, x, y):
        a = x // y
        if a * y == x:
            return [a]
        else:
            pquotients = self.rational_to_contfrac(y, x - a * y)
            pquotients.insert(0, a)
            return pquotients

    def convergents_from_contfrac(self, frac):
        convs = []
        for i in range(len(frac)):
            convs.append(self.contfrac_to_rational(frac[0:i]))
        return convs

    def contfrac_to_rational(self, frac):
        if len(frac) == 0:
            return (0, 1)
        elif len(frac) == 1:
            return (frac[0], 1)
        else:
            remainder = frac[1:len(frac)]
            (num, denom) = self.contfrac_to_rational(remainder)
            return (frac[0] * num + denom, num)

    def is_perfect_square(self, n):
        h = n & 0xF
        if h > 9:
            return -1

        if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
            t = self.isqrt(n)
            if t*t == n:
                return t
            else:
                return -1

        return -1

    def isqrt(self, n):
        if n == 0:
            return 0
        a, b = divmod(n.bit_length(), 2)
        x = 2**(a+b)
        while True:
            y = (x + n//x)//2
            if y >= x:
                return x
            x = y

    def __init__(self, n, e):
        self.d = None
        self.p = None
        self.q = None
        sys.setrecursionlimit(100000)
        frac = self.rational_to_contfrac(e, n)
        convergents = self.convergents_from_contfrac(frac)

        for (k, d) in convergents:
            if k != 0 and (e * d - 1) % k == 0:
                phi = (e * d - 1) // k
                s = n - phi + 1
                discr = s*s - 4*n
                if(discr >= 0):
                    t = self.is_perfect_square(discr)
                    if t != -1 and (s + t) % 2 == 0:
                        self.d = d
                        x = Symbol('x')
                        roots = solve(x**2 - s * x + n, x)
                        if len(roots) == 2:
                            self.p = roots[0]
                            self.q = roots[1]
                        break


def main():
    n, e = 90581, 17993
    # n = 17951889010549737984721918145824663920554679073690113998973505408572333276742641211549442546968910749041370414769716560733410432970403684545646457416752331260877428291280133550133766335892077508492112831750286223965487118118078449455995828306158158087615298950458019018872636464541846556840454887386031286367361384479307310797948820322332930676587832056982407942858657009336823861342639013575571730066646908612580722289096377168906858750133837416305928766138797849452634264807768541741213721334698069410535514648821965761969554985645058070289872573972519446789068431446039745171724897115530486733075929027468539085709
    # e = 9255177507167142640992115273104252200805163770882978057760492509105915396857949293879078511054005577235827085708768831167045390842587585062957494642921811010861109184784686709032635873475486875292991021472964410141501318692753262481398355435957731548292528426001339070251577861110847886108748366618428985360841289665297972636728993183019898021403796030245781826340227545822764255021419145872151942424568692021537123477219364599251751082342131206973867532255034249260929643239644495813782221294729861978022992377755133969736156273046813566502193132634473848456380885594916499296673632186398277871688576908948399894823
    Wiener = WienerAttack(n,e)
    print 'd =', Wiener.d
    print 'p =', Wiener.p
    print 'q =', Wiener.q


if __name__ == '__main__':
    main()
