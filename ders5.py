# for i in range(0,100):
#     if i==55:
#         continue  # 55i pas geç break olursa 54te döngü biter, pass olursa oldugu gibi devam et
#     print(i)

# islem = input("yapmak istredginiz islem(+,-,*,/):")
# sayi1=int(input("sayi gir: "))
# sayi2=int(input("sayi gir: "))
# if islem == "+":
#     pass
# elif islem == "-":
#     pass
# elif islem == "/":
#     pass
# elif islem == "*":
#     pass

# list=[]
# while True:
#     a=input("sayi gir: ")
#     if a=="q":
#         break
#     sayi=int(a)   # int olmazsa str olarak list olusur  
#     list.append(sayi)
# print(list)

# a=int(input("sayi gir: "))
# b=int(input("sayi gir: "))
# toplam=a+b
# print(toplam)

# try:
#     a=int(input("sayi gir: "))
#     b=int(input("sayi gir: "))
#     toplam=a/b
#     print(f"toplam={toplam}")
# except ZeroDivisionError:        # 0a bölünemez hatasını tanımladın    # burda biterse hata oldugunda bütün program coker
#     print("0a bölemezsin")
# except ValueError:
#     print("harf giremezsin")
# except:
#     print("bilinmeyen hata")

# a1=int(input("sayi gir: "))
# ust=a1**4                  # sistem hata verince devam etmesi icin
# print(ust)


dosya=open("burak.txt","w",encoding="utf=8") #burak.txt ders5in içinde bir dosya acacak, w dosyayı hangi kipte acacagını söyler w = yazma kipi
dosya.write("burak karadag")
dosya.write("burak\n")
dosya.close() # tekrar dosyaya yazmak icin open yapman lazım

# dosya=open("burak.txt","r",encoding="utf=8")
# print(dosya.readline()) #ilk satırdaki her seyi yazar = readline
# print(dosya.readlines()) #dosyadaki her satırı liste yapar
# dosya.seek(0) "r" yerine "r+" olursa bu kod calisir indexe göre , r+ = oku yaz

# dosya=open("burak.txt","a",encoding="utf=8")
# dosya.write("\nburakk") # son indexe ekler
# dosya.write("\nburakk")
 
# dosya=open("burak.txt","w+",encoding="utf=8") # her seferinde dosyayi sifirlar, x+ silmeden yapar

with open("burak.txt","r+",encoding="utf-8") as file:
    dosya=file.read()
    dosya=file.write("burak karadag")
    print(dosya)              #bununla dosya acarsan dosya.close a gerek kalmaz, kendi dosyayi kapatir







