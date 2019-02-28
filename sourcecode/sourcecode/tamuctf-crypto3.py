c = 'XUBdTFdScw5XCVRGTglJXEpMSFpOQE5AVVxJBRpLT10aYBpIVwlbCVZATl1WTBpaTkBOQFVcSQdH'

def trans(c, k):
	print k
	m = ''
	for i in range(0, len(c) // k):
		print c[i*k:i*k+k]
	for i in range(0, k):
		for j in range(0, len(c) // k):
			m += c[j*k+i]
	print '\n', m
	return m

t = ''
for i in c:
	t += str(ord(i))
print hex(int(t))
