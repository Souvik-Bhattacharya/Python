# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 23:02:08 2022

@author: Souvik Bhattacharya
"""

#image creation from an RGB value
import numpy as np
from PIL import Image

height = 5
widh = 5
array1 = np.zeros([height,widh,3],dtype = np.uint8)
img = Image.fromarray(array1)
img.save('./static/test0.png')

array2 = np.zeros([100,200,3],dtype = np.uint8)
array2[:,:100] = [255,128,0] #orange
array2[:,100:] = [0,0,255] #blue
im = Image.fromarray(array2)
im.save('./static/test1.png')

#determination of RGB value of an image
I = Image.open('./static/test1.png')
RGB_I = I.convert('RGB')
rgb = RGB_I.getpixel((1,1))
print(rgb)