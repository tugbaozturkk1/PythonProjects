
# başa _ koymazsan math modülünü algılar sürekli hata verir

# import math

# # value = dir(math)  # dir math modülündeki bütün bileşenleri gösterir
# # value = help(math)  # bileşenlerin kullanımını gösterir
# # value = help(math.factorial)
# value = math.sqrt(49) # karekök alma
# value = math.factorial(5)
# value = math.floor(5.9) # aşagi yuvarlama , ceil yukarı yuvarlama
# print(value)



# 1.yöntem
# import math as islem  # math modülü yerine islem yazarak kütüphaneye ulasirsin 
# value = islem.factorial(3)
# print(value)



# 2.yöntem
# from math import * # bütün fonksiyonları import edersin ilgili modülde
# value = factorial(5)
# value = sqrt(9)

# print(value)

# from math import factorial, sqrt

# value = factorial(5)
# value = sqrt(9)
# value = ceil(5.8) # yuakrida import etmedin hata verir

# print(value)



def sqrt(x):
    print("x :" + str(x))

from math import factorial, sqrt

def sqrt(x):
    print("x :" + str(x))   # aynı isimli fonks.dan en son tanımlanan çalişir 

value = sqrt(9)

print(value)



