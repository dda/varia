#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
from PIL import Image
image_file = Image.open(sys.argv[-1])
image_file = image_file.convert('1') # convert
pix = image_file.load()
count=0
mySize=image_file.size
width=mySize[0]
height=mySize[1]
for y in range(0, height):
  x=0
  for x in range (0, width):
    r=0
    for i in range(0, 8):
      c=pix[x, y]
      x=x+1
      if(c>0):
        r=r*2+1
      else:
        r=r*2
    sys.stdout.write(hex(r))
    sys.stdout.write(", ")
  print(" ")
print(" ")
