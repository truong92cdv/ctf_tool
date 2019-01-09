#!/usr/bin/env python3

# e = 65537
# c = 110337659413218270525140479262539535841429742791954874385489
# p = 282174488599599500573849980909
# q = 671998030559713968361666935769
# n = p*q
# phi = (p-1)*(q-1)


e = 0x10001
c = 33062272351573218250384115704487361063970465004033740168733959927707721053321054975845636421337650298670338055101957913137486876401007806540788449215177115739842456860057795240129932234489439409388612936981938930876353938688227847808194010536300529961489751250254640618262254364661940751727869020817391566773
n = 55089599753625499150129246679078411260946554356961748980861372828434789664694269460953507615455541204658984798121874916511031276020889949113155608279765385693784204971246654484161179832345357692487854383961212865469152326807704510472371156179457167612793412416133943976901478047318514990960333355366785001217
q = 7422236843002619998657542152935407597465626963556444983366482781089760759017266051147512413638949173306397011800331344424158682304439958652982994939276427
p = n / q
phi = (p-1)*(q-1)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

d = modinv(e, phi)
m = hex(pow(c, d, n))[2:-1]
flag = m.decode("hex")

print 'p    =  %d' % p
print 'q    =  %d' % q
print 'n    =  %d' % n
print 'phi  =  %d' % phi
print 'e    =  %d' % e
print 'd    =  %d' % d
print 'm    =  %s' % m
print '\nFlag = %s\n' % flag
