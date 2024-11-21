# #metot     class içinde tanımlanır
# list=[1,2,3]
# list.append(4)
# print(list)

# myString="hello"
# print(myString.upper())  #.birseyler = onceden olusturulan kod blogu classla gelir



#fonksiyon   class içinde tanımlanmaz
# anahtar sözcük = def 
# def sayHello():
#     print("Hello")

# sayHello()

def sayHello():
    print("Hello user")

sayHello()

def sayHello(name):
    print("Hello "+ name)

sayHello("tugba")

def sayHello(name = "user"):
    print("hello " + name)

sayHello()

def sayHello(name = "user"):
    return "Hello " + name   # return fonksiyona geri gönderir, ekler

a = sayHello("Tugba")   # tugba bilgisi fonks.a gönderildi ve userin yerine geçti
print(a)


def total(num1,num2):
    return num1+ num2

result=total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2019-dogumYili

ageTugba=yasHesapla(2004)
print(ageTugba)

def EmekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik=65-yas

    if emeklilik > 0:
        print(f"emekliliginize {emeklilik} yil kaldi")
    else:
        print("zaten emekli oldunuz")

EmekliligeKacYilKaldi(1983, "Ali")
EmekliligeKacYilKaldi(1928,"Ahmet")



def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza göre emekliliginize kac yil kaldi
     INPUT: Dogum yili
     OUTPUT:Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik=65-yas

    if emeklilik > 0:
        print(f"emekliliginize {emeklilik} yil kaldi")
    else:
        print("zaten emekli oldunuz")

EmekliligeKacYilKaldi(1983, "Ali")
EmekliligeKacYilKaldi(1928,"Ahmet")

print(help(EmekliligeKacYilKaldi))   # bilgiti verir docstringli kısmı ysni