# def changeName(n):
#     n = "deniz"

# name = "tugba"
# changeName(name)
# print(name)

# def change(n):
#     n[0]="istanbul"  # 0.index istabul olarak degisir

# sehirler = ["ankara", "karabük"]
#                                      # FONKSİYONLU
# change(sehirler)
# print(sehirler)



# sehirler=["ankara","karabük"]
# n=sehirler                           # FONKSİYONSUZ
# n[0]="istanbul"
# print(sehirler)



# def add(a,b):
#     return sum((a,b))  # sum fonks.u pythonla gelen gömülü fonks.dur senden liste bekler
# print(add(10,20))


# def add(a,b, c=0):     # 2 parametreli de 3lü de çalışsın diye c=0
#     return sum((a,b,c))  
# print(add(10,20,3))


# def add(*params):    
#     print(params)        #fazla parametreli
#     return sum((params))  
# print(add(10,20,3,56,98))


# def add(*params):  # tek* tuple listesi göndermek istiyosan kullan 
#     sum = 0        # params farklı kelime de olabilir fark etmez
#     for n in params:  # tek tek elemanları dolaşır for
#         sum = sum + n
#     return sum
# print(add(10,20,3))


# def displayUser(**pargs):   # 2* dictionary geleceği için farklı parametreler için
#     for key,value in pargs.items():
#         print("{} is {}".format(key,value))
# displayUser(name="tugba",age=18,city="karabük")
# displayUser(name="deniz",age=19,city="ankara",phone="12345")


# def myfunc(a,b,*args,**keywordargs):
#     print(a)
#     print(b)           # * a göre terminalde yazar
#     print(args)
#     print(keywordargs)
# myfunc(10,20,30,40,50,key1="value1",key2="value2")


def myfunc(a,b,c,*args,**keywordargs):
    print(a)
    print(b)           
    print(c)
    print(args)
    print(keywordargs)
myfunc(10,20,30,40,50,key1="value1",key2="value2")