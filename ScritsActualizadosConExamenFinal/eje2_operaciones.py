# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:40:01 2020
@author: malen
"""
#Developer: Milena Hernandez
'''
Glossary:
    cv2 functions/methods
    -> cv2 = open cv
    -> imread => image read
    -> add = add images (addition)
    -> imshow  => show the image(s)

Script description:
    1. Download 2 different images.
    2. Apply basic math operations.
    -> Add two images
    -> Subst two images
'''

#import library (ies)
import cv2

def add_images(x, y): #Aqui las imagenes son sumadas
    print(":::here add:::")
    new_image = cv2.add(x, y)
    cv2.imshow('New image', new_image)
    
#main:::::::::::::::::
img_1 = cv2.imread('image/car2.jpg')
img_2 = cv2.imread('image/car2.jpg')

add_images(img_1, img_2)

cv2.waitKey(0)
cv2.destroyAllWindows