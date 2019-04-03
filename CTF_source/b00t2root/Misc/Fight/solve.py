import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow

T = {'OpenParentheses' :'(',
	'CloseParentheses' : ')',
	'Zero' : '0',
	'One' : '1',
	'Two' : '2',
	'Three' : '3',
	'Four' : '4',
	'Five' : '5',
	'Six' : '6',
	'Seven' : '7',
	'Eight' : '8',
	'Nine' : '9',
	'Comma': ','}


f = open('ordinate.txt').read()
for (key, val) in T.items():
	f = f.replace(key, val)
f = f.split('\n')
f = [point.replace(',','').replace('(','').replace(')','').split(' ') for point in f]
# f = [ for point in f]
print f[:10]

im = Image.new("RGB", (500,500))
draw = ImageDraw.Draw(im)
for point in f:
	draw.point((int(point[0]),int(point[1])), fill=point[2])
im.show()
