from PIL import Image 
from PIL import ImageColor
import colorsys
import random
from math import floor

texture = Image.open("./texture/rice.jpg")
image = Image.open("./in/putin.jpg")

tsize = texture.size
isize = image.size

blockSize = 50

data = image.getdata()
print(data[0])

hslImage = []

for pixel in data:
	a,b,c = colorsys.rgb_to_hsv(pixel[0]/255,pixel[1]/255,pixel[2]/255)
	hslImage.append([a,b,c])

hslTexture = []

for pixel in texture.getdata():
	a,b,c = colorsys.rgb_to_hsv(pixel[0]/255,pixel[1]/255,pixel[2]/255)
	hslTexture.append([a,b,c])

for x in hslImage:
	x[2] = 0

s1 = range(len(hslImage)//50)
s2 = set()

for i in range(len(hslTexture)//50):
	print(1)
	temp = []
	for j in range(50):
		temp.append(hslTexture[50*i + j][2])
	s2.add(tuple(temp))

for i in range(len(hslImage)//50):
	temp = s2.pop()
	s2.add(temp)
	for x in range(50):
		hslImage[i*50 + x][2] = temp[x]


rgbImage = []

for p in hslImage:
	a,b,c = colorsys.hsv_to_rgb(p[0],p[1],p[2])
	rgbImage.append((floor(a*255),floor(b*255),floor(c*255)))
out = Image.new('RGB',isize)
out.putdata(tuple(rgbImage))
out.show()
