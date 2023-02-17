#!/usr/bin/python3
# -*- coding: utf-8 -*-

def PlusLongMot(chaine):
    if chaine!=" ":
        l=chaine.split()
        mot= ""
        for x in l:
            if len(mot)<len(x):
                mot=x
        return mot
    else:
        return None