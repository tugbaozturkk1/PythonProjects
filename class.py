# class Person :  
#     # class attributes
#     address = "no information"
#     # constructor (yapıcı metod)
#     def __init__(self, name, year): # self parametre , classtan türetilen herhangi bir objeyi temsil eder
#        # object attributes       # selfin üzerine hangi attributeyi özelligi vermek istiyorsan devamına azarsın
#        self.name = name          # self person oluyor
#        self.year = year
#        print("init metodu calisti")
#     # instance methods
#     def intro(self):
#         print("hello there I am " + self.name)



# # object
# p1 = Person("ali", 1990)
# p2 = Person("yagmur", 1995)
# # update 
# p1.name = "ahmet"
# p1.address = "kocaeli"
# print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
# print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')
# print(p1)
# print(p2)
# print(p1 == p2) # false verir
# p1



class Circle:
    pi = 3.14
    def __init__(self, yaricap=1):
        self.yaricap = yaricap
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
c1 = Circle()
c2 = Circle(5)
print(f"c1 : alan : {c1.alan_hesapla()} cevre : {c1.cevre_hesapla()}")
print(f"c2 : alan : {c2.alan_hesapla()} cevre : {c2.cevre_hesapla()}")




