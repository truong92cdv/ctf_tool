from ec import *

def generate_curve():
	p = 2**160 - 2**32 -  2**14 - 2**12 - 2**9 - 2**8 - 2**7 - 2**3 - 2**2 -1
	a = 1
	b = 7
	E = CurveFp(p, a, b)

	Gx = 1312070859336953328235792006245642608194004626015
	Gy = 183286360807308303108180027093052510417499316608
	G = Point(E, Gx, Gy)

	return E, G


if __name__ == "__main__":
	f = open("flag.txt", "r")
	m = f.read()
	f.close()

	n = int(''.join(format(ord(x), 'b') for x in m),2)

	E, G = generate_curve()
	C = n*G
	print C
	#C = (175725395338760514385959793658960155621853009689,842507576708973597037409970419100653432740595198)