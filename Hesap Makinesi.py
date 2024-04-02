# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:12:10 2024

@author: lenovo
"""

islem = int (input("İslem Numarası Seçiniz :  "))

s1 = float (input("1. Sayı:"))
s2= float (input("2.  Sayı:"))

if(islem==1):
    print("{} + {}={}".format(s1,s2,s1+s2))
elif(islem==2):
    print("{} - {}={}".format(s1,s2,s1-s2))
        
elif(islem==3):
    print("{} * {}={}".format(s1,s2,s1*s2))
    
elif(islem==4):
    print("{} / {}={}".format(s1,s2,s1/s2))

else:
    print("Geçersiz İşlem Numarası")    
    
    
    
    
    
    

    
    
          
          
