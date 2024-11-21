# liste metotları

# sayilar = [-5,2,23,94,5,6,-20,19,94,19,20,31,5,54]
# harfler=["a","b","c","d","g","s","m","h","r"]
# # sonuc = max(sayilar)
# # print(sonuc)
# # sonuc=min(sayilar)
# # print(sonuc)
# # sonuc_harf=max(harfler)
# # print(sonuc_harf)
# # sonuc_harf=min(harfler)
# # print(sonuc_harf)
# # print(sayilar[:6:2])
# # print(harfler[3:7:2])
# # print(sayilar[7])


# # sayilar.append(58)
# # sayilar.insert(3,92)
# # sayilar.pop()
# # sayilar.remove(6)
# # print(len(sayilar))
# # sayilar.sort()
# # sayilar.reverse()
# # print(sayilar.count(5))
# # print(sayilar)
# isimler=["burak","ahmet","mehmet","ahmet","ayse","fatma"]
# # abdulhafiz ismini ekle
# # isimler.append("abdulhafiz")
# # #yasini 2.indexe ekle
# # isimler.insert(2,"yasin")
# # burağı çıkar
# # isimler.pop(0)
# # mehmet kacicnci indexte
# # isimler.sort()
# # isimler.reverse()
# # isimler.remove("ahmet")
# # durum = "fatma" in isimler
# # print(durum)
# for x in isimler:
#     if x=="ahmet":
#         isimler.remove("fatma")

# print(isimler)

# okullar=[]
# x = 1
# while x<=4:
#     okul=input("okulunuzu giriniz:")
#     okullar.append(okul)
#     x+=1
# okullar.sort()
# print(okullar)



# FONKSİYONLAR

# def yas_hesaplama():
#     dogum_tarihi=int(input("lütfen dogum tarihinizi giriniz: "))
#     yas=2023-dogum_tarihi
#     print(f"yasiniz:{yas}")

# yas_hesaplama()

# def yas_hesaplama(dogum_yili):
#     yas=2022-dogum_yili
#     return yas              # fonksiyonun yazıldıgı yere ne koymalıyım returnun amacı

# tugba_yas=yas_hesaplama(2004)
# burak_yas=yas_hesaplama(1992)
# print(tugba_yas,burak_yas)

# def giris_dogrulama(isim,sifre):
#     if isim=="tugba" or sifre=="tugba78":
#         print("giris yapiliyor")
#     else:
#         print("giriş yapilamadi")

# name=input("isminizi giriniz:")
# password=input("dogum yilini gir:")
# giris_dogrulama(name,password)


# gönderilem iki sayi arLRİNDA ASAL Mİ

def asal_mi(a,b):
    for i in range(a,b+1):
        if a>1:
            for x in range(2,a):
                if i%x==0:   # x i y ye böl kalan 0sa cık
                    break
                print(i)
                 





a=int(input("1.sayiyi gir : "))
b=int(input("2.sayiyi griniz: "))
# for i in range(a,b+1):
#     if a>1:
#          for x in range(2,a):
#             if i%x==0:  # x i y ye böl kalan 0sa cık
#                 break
#             else:
#                   print(i)


