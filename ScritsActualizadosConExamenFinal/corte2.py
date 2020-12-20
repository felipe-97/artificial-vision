# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:49:34 2020

@author: malen
"""

import cv2 #OpenCV
import numpy as np
#import matplotlib.pyplot as plt

A = cv2.imread('images/A.jpg')
B = cv2.imread('images/B.jpg')

#Operaciones básicas
pxX = np.size(A, axis=0) #W
pxY = np.size(A, axis=1) #H
pxXY = np.size(A, axis=None)

sumaA = np.sum(A) #SumaA
sumaB = np.sum(B) #SumaB
minimo = np.min(A) #Mínimo

maximo = np.max(A) #Máximo
ARGmaximo = np.argmax(A)
ARGmin = np.argmin(A)
prom = np.mean(A) #Promedio
var = np.var(A) #Varianza
de = np.sqrt(var) #Desviación estándar

#Operaciones avanzadas
#cv2.imshow('Img-Original',img1)

hsv = cv2.cvtColor(A,cv2.COLOR_BGR2HSV)
#cv2.imshow('Img-HSV', hsv)

I = cv2.cvtColor(A,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Img-GRAY', I)
#umbral1 = 50
umbral2,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)  
binaria = np.uint8((I<umbral2)+255)
#cv2.imshow('Img-Binary', binaria)
output = cv2.connectedComponentsWithStats(umbral2,4,cv2.CV_32F)
cantObj = output[0] # Objects quantity

cv2.waitKey(0)
cv2.destroyAllWindows()