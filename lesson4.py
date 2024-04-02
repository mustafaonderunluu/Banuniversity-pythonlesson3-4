# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:23:03 2024

@author: lenovo
"""

# Not Dönüsümü

OrtPuan = int(input("Notunuzu Giriniz : "))

if(OrtPuan >= 90):
    print("AA")
    
elif(OrtPuan >= 80):
    print("BB")    
    
elif(OrtPuan >= 70):
    print("CC") 
    
elif(OrtPuan >= 60):
    print("DD") 

else:
    print("FF")
    
    
    
#Mantıksal Bağlaclar

print (1<5)
print (5<2)

print("YBS"=="ybs")

print ("YBS" or "ybs")

print (3.5 < 8.7 or "YBS" == "ybs")

#Not

print(1)
print(0)
print(not 1)


print(not "python"=="PYTHON" and 1 == 0 or 4.5 < 1.6 or 5 != 5)


print (not True or False)
print (not (True or False))


print ("a"<"z")
print ("a"<"A") #ASCII

#Kullanıcı Girişi 

kullanıcıadı=input(str("Kullanıcı Adı Giriniz :"))
Sıfre=input(str("Sıfre Giriniz :"))


if(kullanıcıadı=="Onder Unlu" and Sıfre == "123456"):
    print("Hoşgeldiniz",kullanıcıadı)
    
elif(kullanıcıadı=="Onder Unlu"):
    print("Kullanıcı Adı Doğru Sifre Hatalı")
    
elif(Sıfre == "123456"):
    print("Sifre Doğru Kullanıcı Adı Hatalı")

else:
    print("Kullanıcı Adı Ve Şifre Yanlıs")
    

#in

print ("a" in "Merhaba")
print(4 in [1,2,3,4])


#for

liste=[1,2,3,4,5]

for i in liste:
    print(i)
    
liste=[1,2,3,4,5]

for i in liste:
    print(i**3)
    
    #Liste içindekileri toplama
liste=[1,2,3,4,5]
toplam = 0
for i in liste:
    toplam += i
    print(toplam)
    
#range
print(*range(5,10))

#Fibonacci Serileri
# a, b = b, a

BirinciSayi=1
ikinciSayi=1

fibonacci=[BirinciSayi,ikinciSayi]
sayac = int (input("Kaç Terim Yazılsın = "))
for i in range(sayac-2):
    BirinciSayi,ikinciSayi=ikinciSayi,BirinciSayi+ikinciSayi
    fibonacci.append(ikinciSayi)
    
print(fibonacci)    
    
    
    
    



