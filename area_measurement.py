# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:37:22 2022

@author: Souvik Bhattacharya
"""
import scipy.misc
import imageio
from PIL import Image
import random
import numpy as np


img = Image.open('westbengal.png')
rgb_img = img.convert('RGB')
count_in = 0
count_wb = 0
count = 0
while(count<=1000000):
    x = random.randint(0,1049)
    y = random.randint(0,1205)
    z = 0
    r,g,b = rgb_img.getpixel((x,y))
    if(r == 136):
        count_in += 1
        count += 1
    elif(r == 5):
        count_wb += 1
        count += 1
area_wb = (count_wb/count_in)*3287263
print(area_wb)

'''
img = imageio.imread("westbengal.png")
count_in = 0
count_wb = 0
count = 0
while(count<=100000):
    x = random.randint(0,1205)
    y = random.randint(0,1049)
    z = 0
    if(img[x][y][z] == 80):
        count_in += 1
        count += 1
    elif(img[x][y][z] == 60):
        count_wb += 1
        count += 1
area_wb = (count_wb/count_in)*3287263
print(area_wb)
'''