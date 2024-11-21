TugbaHesap = {
    "name" : "tugba ozturk",
    "hesapNo" : "12345",
    "bakiye" : 3000,
    "ekHesap" : 2000
}

DenizHesap = {
    "name" : "deniz ozturk",
    "hesapNo" : "123",
    "bakiye" : 2000,
    "ekHesap" : 1000
}

def paraCek(hesap, miktar):
    print(f"hello {hesap['name']}")
    if hesap["bakiye"]>=miktar:
        hesap["bakiye"] -= miktar
        print("parani alabilirsin")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"]+hesap["ekHesap"]
        if toplam >= miktar:
            ekHesapKullanimi = input("ek hesap kullanilsin mi (e/h): ")
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("parani al")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesapta {hesap['bakiye']} bulunmakta")
        else:
            print("bakiye yetersiz")
            bakiyeSorgula(hesap)



def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesapta {hesap['bakiye']} TL bulunmakta ek hesap limiti ise {hesap['ekHesap']} TL bulunmakta")

paraCek(TugbaHesap, 3000)

print("********")
paraCek(TugbaHesap,2000)



