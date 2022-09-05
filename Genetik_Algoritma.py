#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:25:14 2022

@author: barisbalci
"""

import math
from random import random

#İTERASYON SÜRECİ
for dongu in range(0,durma_kriteri):

#Başlangıç çözüm matrisinde yeni bireyleri oluşturabilecek uygun 
#ata(anne ve baba) bireylerin seçilmesi
       for gen in range(0,cn):
          

#birey seçimi için Turnuva Yöntemi kullanılmıştır.
#Problem türü minimizasyon olduğundan uygunluk değeri daha küçük olan bireylerin seçilmesi gerekmektedir.

b1=math.ceil(random()*cn)
b2=math.ceil(random()*cn)
b3=math.ceil(random()*cn)
b4=math.ceil(random()*cn)

#Bu döngüler bireylerin birbirlerinden farklı olması için gerçekleştirilir.

    while(b1==b2) or (b1==b3) or (b1==b4):
        b1=math.ceil(random()*cn)
        while(b2==b3) or (b2==b4):
            b2=math.ceil(random()*cn)
            while(b1==b4) or (b3==b4) or (b3==b2):
                b3=math.ceil(random()*cn)
                while(b1==b4) or (b3==b4) or ( b4==b2):
                    b4=math.ceil(random()*cn)


#ata1: 1. ana birey
#ata2: 1. ana birey
      b1=b1-1
      b2=b2-1
      b3=b3-1
      b4=b4-1
      
      if uygunluk[0][b1]<uygunluk[0][b2]:
          ata1=b1
     else:
         ata1=b2
         
    if uygunluk[0][b3]<uygunluk[0][b4]:
        ata2=b3
    else:
        ata2=b4
        
#ÇAPRAZLAMA İŞLEMİ
#Seçilen iki ata bireyin kromozomları arasında parça değişiminin 
#(çaprazlama) gerçekleştirilmesiyle yeni bir birey oluşturullması

#Parça değişimi için Noktalı Çaprazlama Yöntemi kullanılmıştır.

        ts=...
#c_nok: çaprazlama noktası
    if cp>random():
        c_nok=math.ceil(random()*ts)
        
#Ata bireyler arasında parça değişimi
#yeni: yeni (yavru) kromozom 
#OPT_Y: yeni matris
        
        new[0][0]=OPT[0][ata1]
        new[1][0]=OPT[1][ata1]
        ....
        new[c_nok-1][0]=OPT[c_nok-1][ata1]
        new[c_nok][0]=OPT[c_nok][ata2]
        new[c_nok+1][0]=OPT[c_nok+1][ata2]
        ....
        new[ts-1][0]=OPT[ts-1][ata2]
        
        OPT_Y[0][gen]=new[0][0]
        OPT_Y[1][gen]=new[1][0]
        ....
        OPT_Y[ts-1][gen]=new[ts-1][0]
        
#istenirse 2. yeni birey de oluşturulabilir.
#///yeni2=[OPT(1:c_nok,ata2):OPT(c_nok+1:ts,ata1)]///

#X1yeni: Çaprazlama sonucu x1 tasarım değişkeni için belirlenen yeni değer
#x2yeni: Çaprazlama sonucu x2 tasarım değişkeni için belirlenen yeni değer

        X1new=OPT_Y[0][gen]
        X2new=OPT_Y[1][gen]
        ...
        
        else:
            new=OPT[:][ata1]
            OPT_Y[0][gen]=new[0][0]
            OPT_Y[0][gen]=new[0][1]
       ....
       
       X1new=OPT_Y[0][gen]
       X2new=OPT_Y[1][gen]
       ....

#MUTASYON İŞLEMİ

#mut_gen: mutasyon geçirecek olan gen 
        if random()<mp:
            mut_gen=math.ceil(random()*ts)
            
        if mut_gen==1:
            X1new=Xmin+(Xmaks-Xmin)*random()
            
            OPT_Y[0][gen]=X1new

       if mut_gen==2:
           X2new=Xmin+(Xmaks-Xmin)*random()
       
    OPT_Y[1][gen]=X2new
    .....
    
    
#uygunluk_y: yeni matrite yer alan (local)tasarım değiişkenleri için uygunluk değerinin belirlenmesi
          
           uygunluk_y[0][gen]=OPT_Y[Af][gen]
           
           if uygunluk_y[0][gen]<uygunluk[0][gen]:
               OPT[0][gen]=OPT_Y[0][gen]
               OPT[1][gen]=OPT_Y[1][gen]
               OPT[2][gen=OPT_Y][2][gen]
               
#OPT matrisinin güncellenmesinden dolayı uygunluk değeri de güncellenmelidir.

         uygunluk[0][gen]=OPT[AF][gen]
         
#iterasyon sonu
#deger: tüm iterasyonlar sonucunda elde edilen en iyi çözümü amaç fonksiyonu değeri
#sıra: güncellenen OPT matrisinde bu çözümü yer aldığı vektör 

deger=min(OPT[AF][:])
sira=np.argmin(OPT[AF])


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        