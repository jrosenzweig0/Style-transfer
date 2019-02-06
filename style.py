from PIL import Image 
from PIL import ImageColor
import colorsys
import random
from math import *
from PIL import ImageFilter


class rice:
	__init__(self, color):
		self.color = color
		self.angle = random.randint(0,360)
		self.length = 20 + random.randint(-2,2)
		self.width = 5 + random.randint(-1,1)
		self.image = Image.new('RGB', (40,40))
		# (ecd782) - yellow
		# (d8d9d1) - cream
		# (e7e8e2) - white
 	draw(self):

 	boundingFunction(self, x, y):
 		if(abs(x-20)>self.length/2):
 			return (0,0,0)
 		if(abs(y-20)>self.width/2):
 			return (0,0,0)
 		if(abs(abs(x-20)*abs(x-20) + 16*abs(y-20)*abs(y-20)) > self.length*self.length*0.25):
 			return (0,0,0)
 		if(abs(y-20-sqrt((100-(x-20)*(x-20))/80))<0.12):
 			return((white))
 		if((x-23)*(x-23) + 64*(y-19.5)*(y-19.5) <= 16):
 			return(yellow)
 		else:
 			return cream







texture = Image.open("./texture/rice.jpg").crop((0,0,800,536))
image = Image.open("./in/putin.jpg").crop((29,0,829,536))
edges = image.filter(ImageFilter.FIND_EDGES)

tsize = texture.size
isize = image.size

blockSize = 50

data = image.getdata()
print(data[0])

hslImage = []
lightnessfilter = []

for pixel in edges.getdata():
	if pixel[0] + pixel[1] + pixel[2] > 55:
		lightnessfilter.append(1)
	else:
		lightnessfilter.append(0)

for pixel in data:
	a,b,c = colorsys.rgb_to_hsv(pixel[0]/255,pixel[1]/255,pixel[2]/255)
	hslImage.append([a,b,c])


hslTexture = []

for pixel in texture.getdata():
	a,b,c = colorsys.rgb_to_hsv(pixel[0]/255,pixel[1]/255,pixel[2]/255)
	hslTexture.append([a,b,c])

count = 0
for pixel in hslImage:
	pixel[0] = floor(pixel[0]*255)
	pixel[1] = floor(hslTexture[count][1]*255)
	if lightnessfilter[count] == 0:
		pixel[2] = floor(hslTexture[count][2]*255)
	else:
		pixel[2] = floor(pixel[2]*255)

	count += 1

for i in range(len(hslImage)):
	hslImage[i] = tuple(hslImage[i])

hslImage = tuple(hslImage)

out = Image.new('HSV', (800, 536))

out.putdata(hslImage)
out.filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.SMOOTH_MORE).show()


