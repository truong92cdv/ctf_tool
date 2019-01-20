# phi = (p-1)*(q-1)

# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     g, y, x = egcd(b%a,a)
#     return (g, x - (b//a) * y, y)

# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('No modular inverse')
#     return x%m

# d = modinv(e, phi)



n = 17951889010549737984721918145824663920554679073690113998973505408572333276742641211549442546968910749041370414769716560733410432970403684545646457416752331260877428291280133550133766335892077508492112831750286223965487118118078449455995828306158158087615298950458019018872636464541846556840454887386031286367361384479307310797948820322332930676587832056982407942858657009336823861342639013575571730066646908612580722289096377168906858750133837416305928766138797849452634264807768541741213721334698069410535514648821965761969554985645058070289872573972519446789068431446039745171724897115530486733075929027468539085709
e = 9255177507167142640992115273104252200805163770882978057760492509105915396857949293879078511054005577235827085708768831167045390842587585062957494642921811010861109184784686709032635873475486875292991021472964410141501318692753262481398355435957731548292528426001339070251577861110847886108748366618428985360841289665297972636728993183019898021403796030245781826340227545822764255021419145872151942424568692021537123477219364599251751082342131206973867532255034249260929643239644495813782221294729861978022992377755133969736156273046813566502193132634473848456380885594916499296673632186398277871688576908948399894823
c = 13685824754412294767161870154394935171662372556882324072712215825247647777622476307499584456736325913095222244370882491480789672981245694439851052456050523584833628015770017973372002306829891018406870737397171684344383278099231627004851215523325774892491161074742034905463041064379100975545674569478355475517372568602747675072875872365932640799775995640879558478611608524540608348459813065152176210263410374897800276932756067418824325121488395796729583891948687986914406684160387625610994211955475639821415792810780918340686757298888282065017600884226293750275711934514199531243034570947080752198566937262329778067535
d = 340282366920938463463374607431768211447

m = hex(pow(c, d, n))[2:-1]
flag = m.decode("hex")

print '\nFlag = %s\n' % flag