# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:47:29 2020

@author: malen

import cv2
aux = []
numbers = [5,3,8,10,20,2,4,1]

def reverse_numbers():
    last_pos = len(numbers)-1
    
    while last_pos >= 0 :
        aux.append(numbers[last_pos])
        last_pos -=1
    return aux

#Main
print (numbers)
res = reverse_numbers()

"""
import cv2
list = ["1,2,3,4,7", "7,8,9,10,5"]

listA = list[0].split(sep=',')
listB = list[1].split(sep=',')

i=0
counter=0

while i < len(listA) :
    j=0
    while j < len(listB) :
        if listA[i] == listB[j] :
             print (listA[i])
             counter+=1
             j+=1
             i+=1
        if counter == 0:
            print("None")


cv2.waitKey(0)
cv2.destroyAllWindows