#!/usr/bin/python3
# -*- coding: utf-8 -*-

def credit(l):
    for i in range(len(l)):
        a=l[0]
        b=l[1]
        c=l[2]
        salaire=l[3]
        Icredit=a*(b)
        Icredit+=a
        Ncredit=Icredit*c
        Ncredit2= a+Ncredit
    if salaire>0:
        if Ncredit2>=salaire*12:
            return  0
        else:
            return Ncredit2
    else:
        return "salaire insuffisant"