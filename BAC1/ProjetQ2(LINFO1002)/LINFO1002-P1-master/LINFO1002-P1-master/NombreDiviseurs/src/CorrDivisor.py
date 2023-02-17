#!/usr/bin/python3
# -*- coding: utf-8 -*-


def divisor(liste):
    l=[]
    l1=[]
    a=liste[0]
    b=liste[1]
    if a==b:
        return None
    elif a>0 and b>0:
        for i in range(2,a):
            if a%i==0:
                l.append(i)
        for j in range(2,b):
            if b%j==0:
                l1.append(j)
        if len(l)>len(l1):
            return len(l)
        else: 
            return len(l1)
    elif a<0 and b<0:
        return -1
    else:
        return []


   
