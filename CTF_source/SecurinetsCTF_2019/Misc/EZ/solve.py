from PIL import Image
import binascii

im = Image.open('pic.png')
pix_val = list(im.getdata())
lsbs=""
for idx,val in enumerate(pix_val):
	# Converting each rgb values into binary and keeping only the Least Significant Bit 
	lsbs=lsbs+'{0:08b}'.format(val[0])[-1]  
	lsbs=lsbs+'{0:08b}'.format(val[1])[-1]
	lsbs=lsbs+'{0:08b}'.format(val[2])[-1]
n=int(lsbs,2)
# Converting binary to ascii 
print binascii.unhexlify('%x' % n)