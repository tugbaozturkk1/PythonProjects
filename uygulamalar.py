# x, y, z = 2, 5, 10
# numbers = 1, 5, 7, 10, 6

# sayi=int(input("1.sayiyi giriniz: "))
# sayi2=int(input("2.sayiyi giriniz: "))
# print((sayi*sayi2)-(x+y+z))

# a=y//x
# print(a)

# print((x+y+z)%3) # 17nin 3e bölm kalan

# print(y**x)

# x, *y, z = numbers
# print(z**3)     # x=1 y=[5,7,10] z=6

# x, *y, z = numbers
# print((y[0]) + (y[1]) + (y[2]) )

# password = "2878"
# username = "tuugbaozturkk"

# w = (username == "tgbozt") # esit mi demek
# w = (password != "7828")   # esit degil mi demek

# print(w)



# num1= int(input("1.sayiyi griniz: "))
# num2= int(input("2.sayiyi griniz: "))
# print(num1)
# print(num2)
# print(num1 > num2)


# a = float(input("1.vize notu: "))
# b = float(input("2.vize notu: "))
# c = float(input("final notu: "))
# ort = ((a+b)*6/10)+(c*4/10)
# print(f"not ort: {ort} ve dersten gecme durumunuz: {ort>=50}")


# a = float(input("1.vize notu: "))
# b = float(input("2.vize notu: "))
# c = float(input("final notu: "))
# ort = ((a+b)/2*6/10)+(c*4/10)
# if ort<50:
#     print("kaldiniz bb")
# else:
#     print("aferin gectin")



# a = int(input("sayi gir: "))
# if a%2==0:  # mod 2sini alınca 0 çıkar yani kalan 0
#     print("cift")
# else:
#     print("tek")


# w = float(input("sayi: "))
# if w<0:
#     print("negatif")
# else:
#     print("pozitif")



# email="tgb@gmil.com"
# password = "1t"
# mail=input("email: ")
# p=input("password: ")
# a = email == mail
# b = password == p
# print(f"email {a} ve parola {b}")



# a = input("name: ")
# b = int(input("age: "))
# c = input("education: ")
# if b>=18 and (c=="high school" or c=="university"):
#     print("ehliyet alabilirsiniz")
# else:
#     print("alamazsiniz")


# a = int(input("1.sinav: "))
# b = int(input("2.sinav: "))
# c = int(input("sözlü: "))
# ort = (a+b+c)/3
# if ort < 24 and ort>0:
#     print("0")
# elif ort < 44 and ort>25:
#     print("1")
# elif ort < 54 and ort>45:
#     print("2")
# elif ort < 69 and ort>55:
#     print("3")
# elif ort < 80 and ort>70:
#     print("4")
# else:
#     print("5")

# import datetime
# x = datetime.datetime(2004,1,19)
# print(x)

# import datetime
# x = datetime.datetime(2004,1,19)
# print(x.strftime("%B"))


# numbers = [1,3,5,7,9,12,19,21]

# for num in numbers:
#     if num%3==0:
#         print(num)
        

# result = 0
# for sayi in numbers:
#     result += sayi
# print(result)



# for num in numbers:
#     if num%2==1:   # tek sayi 
#         print(num**2)



cities = ["kocaeli","istanbul","ankara","izmir","rize"]

# for city in cities:
#     if len(city)<=5:
#         print(city)


# products = [
#     {"name":"redmi note 8", "price":"3500"},
#     {"name":"redmi note 9", "price":"4000"},
#     {"name":"redmi note 10", "price":"5000"}
# ]

# result = 0
# for ürün in products:
#     fiyat = int(ürün["price"])
#     result += fiyat
# print(result)

# for urun in products:
#     if int(urun["price"])<=5000:
#         print(urun["name"])



# sayilar = [1,3,5,7,9,12,19,21]

# for x in sayilar:
#     print(x)
# #   ya da 
# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1  # sonsuz döngüye girmemesi için

# bas = int(input("ilk sayi: "))
# son = int(input("son sayi: "))
# while bas < son:
#     bas += 1 
#     if bas % 2 == 1:
#         print(bas)
    


# w = 100
# while w > 0:
#     print(w)
#     w -= 1



# number = []
# a = int(input("1.sayi: "))
# b = int(input("2.sayi: "))
# number.append(a)
# number.append(b)
# number.sort()
# print(number)



# products = []
# num = int(input("number of products: "))
# w = 0
# while w < num:
#     name = input("name of product: ")
#     price = int(input("price of product: "))
#     products.append({
#         "name" : name,
#         "price" : price
#     })
#     w += 1

# for product in products:      # dışarda çift tırnaksa içerde tek tırnak ya da tersi
#     print(f"name of product: {product['name']} , price of product: {product['price']}")




# import random
# sayi = random.randint(1,10)
# can = int(input("kac can istersin: "))
# hak = can
# sayma = 0
# while hak > 0:
#     hak -= 1
#     sayma += 1
#     tahmin = int(input("tahmin: "))
#     if sayi == tahmin:
#         print(f"tebrik {sayma} defada bildin puan: {100 - (20)*(sayma-1)}")
#         break
#     elif sayi > tahmin:
#         print("yukarı")
#     else:
#         print("asagi")


#     if hak == 0:
#         print(f"hak bitti tutulan sayi {sayi}")





# sayi = int(input("sayi gir: "))
# asalMi = True  # basta girilen sayi asal kabul edilir (varsayim olarak)
# if sayi == 1 :
#     asalMi = False
# for w in range(2,sayi):
#     if sayi % w == 0: # bölününce 0 kalansa tam bölen yani asal değil
#         asalMi = False
#         break
# if asalMi :
#     print("asal")
# else:
#     print("asal degil")








# def yaz(kelime, adet):
#     print(kelime * adet)   # gönderilen kelimeyi belirtilen kez yaz

# yaz("hello\n",3)




# def listeyeCevir(*a):         # kendine gönd sınırsız parametreyi bir listeye çeviren fonks yaz
#     liste = []

#     for b in a:
#         liste.append(b)
    
#     return liste
# result = listeyeCevir(1,2,3,"hello")
# print(result)





# gönderilen 2 sayı arası asalları bul
# def asalSayiBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):   # +1 sayi2de dahil olsun diye
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#                 else:
#                     print(sayi)

# sayi1 = int(input("1.sayi: "))
# sayi2 = int(input("2.sayi: "))

# asalSayiBul(sayi1,sayi2)







# gönd sayının tam bölenlerini liste şeklinde geri gönder
# def tamBoleniBul(sayi):
#     tamBolen = []
#     for i in range(2,sayi):
#         if (sayi % i == 0):
#             tamBolen.append(i)
#     return tamBolen
# print(tamBoleniBul(117))


# def not_hesapla(satir):
#     satir = satir[:-1]
#     liste = satir.split(":")
#     ogrenciAdi= liste[0]
#     notlar = liste[1].split(",")
    
#     not1 = int(notlar[0])
#     not2 = int(notlar[1])
#     not3 = int(notlar[2])

#     ortalama = (not1+not2+not3)/3

#     if ortalama>90 and ortalama<=100:
#         harf = "AA"
#     elif ortalama>=85 and ortalama<=89:
#         harf = "BA"
#     elif ortalama>=65:
#         harf = "CC"
#     else:
#         harf = "FF"
#     return ogrenciAdi + ": " + harf + "\n"

# def ort_oku():
#     with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
#         for satir in file:
#             print(not_hesapla(satir))
# def not_gir():
#     ad = input("ogrenci adi: ")
#     soyad = input("ogrenci soyadi: ")
#     not1 = input("1.not: ")
#     not2 = input("2.not: ")
#     not3 = input("3.not: ")

# #     with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
# #         file.write(ad+' '+ soyad+ ':' +not1+','+not2+','+not3+'\n')
# # def not_kayit():
# #     pass
# # while True:
# #     islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Ckıs\n")
# #     if islem == "1":
# #         ort_oku()
# #     elif islem == "2":
# #         not_gir()
# #     elif islem == "3":
# #         not_kayit()
# #     else:
# #         break 


# strvar = "Yakin Kampüs"
# # print(strvar[10])
# print(strvar.index("ü"))
# print(strvar.upper().lower()) # önce büyültür sonra küçültür

# list = [1 , 2 , True , "a"]
# x = len(list) == len(set(list))
# print(x)



# kullanici1 = {
#     "ad": "Ferhat",
#     "soyad": "Ibrik",
#     "uzmanlik": ["Front-End"]
# }
# kullanici2 = {
#     "ad": "Gokce",
#     "soyad": "Gun",
#     "uzmanlik": ["Tasarim"]
# }
# kullanici3 = {
#     "ad": "Mesut",
#     "soyad": "Gun",
#     "uzmanlik": ["Front-End"]
# }
# print(kullanici1["uzmanlik"])

# kullanicilistesi = [kullanici1, kullanici2, kullanici3]
# for kullanici in kullanicilistesi:
#     if "Front-End" in kullanici["uzmanlik"]:      # if kullanici["uzmanlik"] == ["Front-End"]  dersen mesuta yazılım eklenince sadece ferhatş veir
#         print(kullanici["ad"])                                    
    
# kullanici3["uzmanlik"].append("yazilim") 
# print(kullanici3)

# if len(kullanici["uzmanlik"]) > 1:
#     print(kullanici)

# kullanici_yaslari_listesi = [22, 34, 32]
# for kullanici, yas in zip(kullanicilistesi, kullanici_yaslari_listesi):
#     if yas < 30:
#         print(kullanici)

# deger = int(input("sayi giriniz: "))
# if deger == 0:
#     print("sayi nötr")
# elif deger == 1:
#     print("1 asal değil")
# elif deger == 2:
#     print("2 asal")
# elif deger%2==1:
#     print("sayi asal")
# else:
#     print("asal değil")


# def number_input_control():
#     girdi = input("Write a number: ")
#     if girdi.isdigit():  # is digit rakam mı demek
#         print("Congratulations! You wrote a number. ")
#     else:
#         print("Sorry! You did not write a number. ")


# def number_input_control_loop():
#     girdi = input("Write a number: ")
#     again = 0
#     while not girdi.isdigit():
#         print("Sorry! It was not a number. ")
#         girdi = input("Write a number: ")
#         again += 1
#         if again > 5:
#             break
        
#     else:
#         print("Congratulations! You wrote a number. ")

# number_input_control_loop()



# def ustel_sayi_v2(num1, num2):
#     result = 1
#     for kuvvet in range(1, num2+1):
#         result = result*num1
#     print(result)

# ustel_sayi_v2(9, 2)










