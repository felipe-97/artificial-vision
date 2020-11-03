# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:35:43 2020

@author: HP-ProBook 440
    
luis felipe lopez enriquez 

"""            
              
import numpy as np      
import cv2       
import matplotlib.pyplot as plt
   
        
# :::::: ORIGINALES IMAGES ::::::
img1 = cv2.imread('Setimagenes/A.jpg')        
img2 = cv2.imread('Setimagenes/B.jpg')   

# :::::: Escala de grises ::::::
I = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('Img-A', I)   

A = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('Img-B', A)

#Operaciones básicas imagen A
pxX = np.size(img1, axis=0) #W
pxY = np.size(img1, axis=1) #H
pxXY = np.size(img1, axis=None)

promManual = np.sum(img1) / (pxX * pxY * 3)

suma = np.sum(img1) #Suma
minimo = np.min(img1) #Mínimo
maximo = np.max(img1) #Máximo
prom = np.mean(img1) #Promedio
var = np.var(img1) #Varianza
de = np.sqrt(var) #Desviación estándar

#Operaciones básicas imagen B
pxXB = np.size(img2, axis=0) #W
pxYB = np.size(img2, axis=1) #H
pxXYB = np.size(img2, axis=None)

promManualB = np.sum(img2) / (pxX * pxY * 3)

sumaB = np.sum(img2) #Suma
minimoB = np.min(img2) #Mínimo
maximoB = np.max(img2) #Máximo
promB = np.mean(img2) #Promedio
varB = np.var(img2) #Varianza
deB = np.sqrt(var) #Desviación estándar

# ::::::  formato Binario ::::::
umbralA,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
binaria = np.uint8((I<umbralA)+255)
cv2.imshow('Img-Binary', binaria)

umbralB,_ = cv2.threshold(A,0,255,cv2.THRESH_OTSU)
binaria2 = np.uint8((A<umbralB)+255)
cv2.imshow('Img-Binary2', binaria2)

#
mascara = np.uint8((I<umbralA)+255) #Binary image
output = cv2.connectedComponentsWithStats(mascara,0,cv2.CV_32F)
cantObj = output[0] # Objects quantity
labels = output[1] # Labels
stats = output[2]

mascaraB = np.uint8((A<umbralB)+255) #Binary image
outputB = cv2.connectedComponentsWithStats(mascaraB,0,cv2.CV_32F)
cantObjB = outputB[0] # Objects quantity
labelsB = outputB[1] # Labels
statsB = outputB[2]

resA = cv2.add(img1,img2)
cv2.imshow('resA',resA)

#Histograma
data = I.flatten()
red = img1[:,:,0].flatten()
green = img1[:,:,1].flatten()
blue = img1[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")

#Histograma B 
dataB = A.flatten()
redB = img2[:,:,0].flatten()
greenB = img2[:,:,1].flatten()
blueB = img2[:,:,2].flatten()

plt.hist(dataB,bins=100)
plt.hist(redB, bins=1000, histtype="stepfilled", color="red")
plt.hist(greenB, bins=1000, histtype="stepfilled", color="green")
plt.hist(blueB, bins=1000, histtype="stepfilled", color="blue")

cv2.waitKey(0)
cv2.destroyAllWindows()