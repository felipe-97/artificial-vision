# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:53:24 2020

@author: malen
"""
import numpy as np
import cv2
import matplotlib as plt

img = cv2.imread('image/bananaPDI.jpg')

I = cv2.cvtColor(img, cv2.COLOR_BG2GRAY)

binary = np.uint8((I<200)*255)
