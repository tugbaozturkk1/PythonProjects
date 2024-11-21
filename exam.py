# 1.soru
import datetime
birthday = datetime.datetime(2004,1,19)
now = datetime.datetime.now()
date = now-birthday
print(f"{int(date.days / 365.2425)} yil yasindasiniz")

# 2.soru
import random
list = []
x=0
while x<100:
    a = random.randint(0,1024)
    if a>850:
        list.append(a)
    x+=1
print(list)


# 3.soru
ürünler = {
    "muz" : 21.50,
    "elma" : 19.50,
    "armut" :29.90 ,
    "karpuz":19.90,
    "makarna":11.75,
    "mercimek": 22.50,
    "ekmek" :5
}
result = 0
def urunAl():
    alinan = input("hangi urunu istersiniz: ")
    if alinan=="quit":
        return
    adet = float(input("kac adet istersiniz: "))
    global result
    result += ürünler[alinan]*adet
    urunAl()
for urun in ürünler:
    print(f"{urun} {ürünler[urun]}")
urunAl()
print(result)

# 5.soru
class Person:
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname=surname
        self.salary=salary
    def zamla(self, amount):
        self.salary=self.salary + self.salary*float(amount)
        return self.salary

tugba=Person("Tugba", "Ozturk", 3000)
deniz = Person("Deniz", "Ozturk", 3000)
tugba.zamla(10)
deniz.zamla(15)
print(tugba.salary)
print(deniz.salary)