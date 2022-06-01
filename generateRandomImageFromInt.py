# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 23:32:47 2022

@author: Diana Cristina Culincu
"""

import random
import numpy as np
from PIL import Image

im = Image.new("RGB", (300,300))
im = np.array(im)

for r in range(0,300):
    for c in range(0,300):
        re = random.randint(0, 255)
        gr = random.randint(0, 255)
        bl = random.randint(0, 255)
        im[r][c]=[re,gr,bl]
img = Image.fromarray(im, 'RGB')

img.show()