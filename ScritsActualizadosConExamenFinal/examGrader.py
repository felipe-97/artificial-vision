# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:04:53 2020

@author: malen
"""

import cv2 #OpenCV
import numpy as np

#imgExam1 = cv2.imread('image/Cal_1.jpg',0)
imgExam2 = cv2.imread('image/Cal_2.jpg',0)
#mgExam3 = cv2.imread('image/Cal_3.jpg',0)

#cv2.imshow('::: Exam_1 - Source:::', imgExam1)

#1. CANNY
can = cv2.Canny(imgExam2,20,150)
kernel = np.ones((5,5),np.uint8)
bordes = cv2.dilate(can,kernel)

contours,_= cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Dibujar contornos
objects = bordes.copy()
cv2.drawContours(
    objects,
    [max(contours, key=cv2.contourArea)],-1,255,thickness=-1)


#Get labels
output  = cv2.connectedComponentsWithStats(objects,0,cv2.CV_32S)
cantObj = output[0] # Cantidad de objetos
labels = output[1] # etiquetas
stats = output[2]

#Get ARGMax
mask = np.uint8(255*(np.argmax(stats[:,4][1:])+ 1==labels))

contours,_= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

#convexHulll => Poligonos
hull = cv2.convexHull(cnt)
puntoConvex = hull[:,0:]
m,n = mask.shape
ar = np.zeros((m,n))
mascara_convex = np.uint8(cv2.fillConvexPoly(ar,puntoConvex,1))


cv2.waitKey(0)
cv2.destroyAllWindows