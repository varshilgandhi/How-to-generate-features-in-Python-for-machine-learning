# -*- coding: utf-8 -*-
"""
Created on Mon May 10 03:57:59 2021

@author: abc
"""

# Entropy Filter

import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk

img = cv2.imread('scratch.jpg')

#convert image into gray level image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply entropy filter
entropy_img = entropy(img, disk(1))

cv2.imshow('Original image', img)
cv2.imshow('Entropy',entropy_img)
cv2.waitKey()
cv2.destroyAllWindows()

###################################################################

#Entropy Filter

import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk

img = cv2.imread('Yeast_Cells.png')

#convert image into gray level image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply entropy filter
entropy_img = entropy(img, disk(1))

cv2.imshow('Original image', img)
cv2.imshow('Entropy', entropy_img)
cv2.waitKey()
cv2.destroyAllWindows()


##################################################################


#Gaussian filter

import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk

img = cv2.imread('Yeast_Cells.png')

#Convert image into gray level image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply entropy filter
entropy_img = entropy(img, disk(1))

#Apply gaussian filter

from scipy import ndimage as nd
gaussian_img = nd.gaussian_filter(img, sigma=3)

cv2.imshow('Original image', img)
cv2.imshow('Gaussian', gaussian_img)
cv2.waitKey()
cv2.destroyAllWindows()

####################################################################

#Sobel filter 

import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk

img = cv2.imread('Yeast_Cells.png')

#Convert image into gray level image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
#Apply entropy filter
entropy_img = entropy(img, disk(1))

#Apply gaussian filter
from scipy import ndimage as nd
gaussian_img = nd.gaussian_filter(img, sigma=3)

#Apply sobel filter
from skimage.filters import sobel
sobel_img = sobel(img)

cv2.imshow('Original image', img)
cv2.imshow('Sobel image', sobel_img)
cv2.waitKey()
cv2.destroyAllWindows()

###############################################################

#how to put all the information together 
#Using pandas dataframe we can do this

import cv2
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel
import pandas as pd

img = cv2.imread('Yeast_Cells.png')

#Convert image into gray level image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Reshape our image
img2 = img.reshape(-1)

#create pandas dataframe
df = pd.DataFrame()
df['Original Pixel Values'] = img2

#Entropy filter
entropy_img = entropy(img, disk(1))
entropy1 = entropy_img.reshape(-1)
df['Entropy'] = entropy1

#Gaussian filter
gaussian_img = nd.gaussian_filter(img, sigma=3)
gaussian1 = gaussian_img.reshape(-1)
df['Gaussian'] = gaussian1

#Sobel filter
sobel_img = sobel(img)
sobel1 = sobel_img.reshape(-1)
df['Sobel'] = sobel1

#print our dataframe
print(df)


















 













 


















