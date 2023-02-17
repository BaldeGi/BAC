#!/usr/bin/python3
# -*- coding: utf-8 -*-

def average(l):
    if l!=[]:
        sum=0
        for i in l:
            sum+=i
            k= sum/len(l)
        return k
    else:
        return None
   
