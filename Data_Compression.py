# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:45:43 2022

@author: Souvik Bhattacharya
"""

import numpy
from PIL import Image
im = Image.open('image.png')
pixelmap = im.load()
I = numpy.asanyarray(Image.open('image.png'))
img = Image.new(im.mode,im.size)
pixel_new_map = img.load()
'''
to save that into 3 bit file it should be reduced by 5 bit
0-31=0
32-63=1
64-95=2
96-127=3
128-159=4
160-191=5
192-223=6
224-255=7
'''
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if(pixelmap[i,j]>=0 and pixelmap[i,j]<=31):
            pixel_new_map[i,j] = 0
        elif(pixelmap[i,j]>=32 and pixelmap[i,j]<=63):
            pixel_new_map[i,j] = 1
        elif(pixelmap[i,j]>=64 and pixelmap[i,j]<=95):
            pixel_new_map[i,j] = 2
        elif(pixelmap[i,j]>=96 and pixelmap[i,j]<=127):
            pixel_new_map[i,j] = 3
        elif(pixelmap[i,j]>=128 and pixelmap[i,j]<=159):
            pixel_new_map[i,j] = 4
        elif(pixelmap[i,j]>=160 and pixelmap[i,j]<=191):
            pixel_new_map[i,j] = 5
        elif(pixelmap[i,j]>=192 and pixelmap[i,j]<=223):
            pixel_new_map[i,j] = 6
        elif(pixelmap[i,j]>=224 and pixelmap[i,j]<=255):
            pixel_new_map[i,j] = 7
img.save('image_new.png')
J = numpy.asanyarray(Image.open('image_new.png'))