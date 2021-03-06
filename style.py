from PIL import Image 
from PIL import ImageColor
import colorsys
from random import randint
from math import *
from PIL import ImageFilter
import sys


class rice:
	def __init__(self, color, angle=randint(0,360)):
		self.color = color
		self.angle = angle
		self.length = 20 + randint(-2,2)
		self.width = 5 + randint(-1,1)
		self.image = Image.new('RGB', (40,40))

	def draw(self):
		temp = []
		for y in range(40):
			for x in range(40):
				temp.append(self.coloringFunction(x,y))
		self.image.putdata(tuple(temp))
		self.image = self.image.filter(ImageFilter.SMOOTH).rotate(self.angle)


	def coloringFunction(self, x, y):
		if(abs(abs(x-20)*abs(x-20) + 16*abs(y-20)*abs(y-20)) > self.length*self.length*0.25):
			return (0,0,0)
		if(x >= 12 and x <=28 and abs(y-20-sqrt((100-(x-20)*(x-20))/80))<0.12):
			return (int(((231 + randint(-3,3))*self.color[0])//255) ,int(((232 + randint(-3,3))*self.color[1])//255) ,int(((226 + randint(-3,3))*self.color[2])/255))
		if((x-23)*(x-23) + 64*(y-19.5)*(y-19.5) <= 18):
			return (int(((236 + randint(-3,3))*self.color[0])//255) ,int(((215 + randint(-3,3))*self.color[1])//255) ,int(((130 + randint(-3,3))*self.color[2])/255))
		else:
			return (int(((216 + randint(-3,3))*self.color[0])//255) ,int(((217 + randint(-3,3))*self.color[1])//255) ,int(((209 + randint(-3,3))*self.color[2])/255))


def grad(pixel1, pixel2, pixel3):
	p1 = (pixel1[0] + pixel1[1] + pixel1[2])/3
	p2 = (pixel2[0] + pixel2[1] + pixel2[2])/3
	p3 = (pixel3[0] + pixel3[1] + pixel3[2])/3
	x = p1-p2

	if(x == 0):
		return 90
	y = p1-p3
	return (atan(y/x)*180/pi)+90




# texture = Image.open("./texture/rice.jpg").crop((0,0,800,536))
image = Image.open("./in/" + sys.argv[1])
# edges = image.filter(ImageFilter.FIND_EDGES)

# tsize = texture.size
isize = image.size

output = Image.new('RGB', (isize[0]+40, isize[1]+40))
n = 0
for i in range(floor(isize[0]*isize[1]/16)):
	if(i%int(isize[0]*isize[1]/1000) == 0):
		sys.stdout.write("\b" * (n))
		x = str(round(100*((16*i)/(isize[0]*isize[1])),1))
		sys.stdout.write(x)
		n = len(x)
		sys.stdout.flush()

	x = randint(0,isize[0]-1)
	y = randint(0,isize[1]-1)
	temp1 = image.getpixel((x,y))
	if x == isize[0]-1 or y == isize[1]-1:
		Rice = rice(temp1)
	else:
		Rice = rice(temp1, grad(image.getpixel((x,y)),image.getpixel((x+1,y)),image.getpixel((x,y+1))))
	Rice.draw()
	for y11 in range(22):
		y1 = y11+9
		for x11 in range(22):
			x1 = x11 + 9
			temp = Rice.image.getpixel((x1,y1))
			if temp[0] + temp[1] + temp[2] < 40:
				continue
			else:
				output.putpixel((x+x1,y+y1), temp)

output.show()
output.save('./out/' + sys.argv[1])
# blockSize = 50

# data = image.getdata()


# hslImage = []
# lightnessfilter = []

# for pixel in edges.getdata():
# 	if pixel[0] + pixel[1] + pixel[2] > 55:
# 		lightnessfilter.append(1)
# 	else:
# 		lightnessfilter.append(0)

# for pixel in data:
# 	a,b,c = colorsys.rgb_to_hsv(pixel[0]/255,pixel[1]/255,pixel[2]/255)
# 	hslImage.append([a,b,c])


# hslTexture = []

# for pixel in texture.getdata():
# 	a,b,c = colorsys.rgb_to_hsv(pixel[0]/255,pixel[1]/255,pixel[2]/255)
# 	hslTexture.append([a,b,c])

# count = 0
# for pixel in hslImage:
# 	pixel[0] = floor(pixel[0]*255)
# 	pixel[1] = floor(hslTexture[count][1]*255)
# 	if lightnessfilter[count] == 0:
# 		pixel[2] = floor(hslTexture[count][2]*255)
# 	else:
# 		pixel[2] = floor(pixel[2]*255)

# 	count += 1

# for i in range(len(hslImage)):
# 	hslImage[i] = tuple(hslImage[i])

# hslImage = tuple(hslImage)

# out = Image.new('HSV', (800, 536))

# out.putdata(hslImage)
# out.filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.SMOOTH_MORE).show()


