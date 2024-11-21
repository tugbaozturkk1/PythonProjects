# scope = kapsam
# scope = global ve lokal değişkenler
x = "global x"  # global scope
def function():
    x = "local x"  # local scope
function()
print(x)
# fonks. yeni bir tanımlama,çalışma alanı oluşturur ve fonks. içindeki değişkenşer disaridaki degiskenleri etkilemez


x = "global x"  
def function():
    x = "local x" 
    print(x)    # fonks kapsaminda tanımlandigi icin terminalde yazar
function()
print(x)



x = "global x"  
def function():
    print(x)    # 2 kere global gelir fonks içinde tanımlama yok dolayısıyla global olan kapsamı alır
function()
print(x)


#############################################

name = "tugba"   # global
def changeName(newName):
    name = newName              # önce lokal sonra global
    print(name)   # local
changeName("deniz")
print(name)

##########################################

name = "global string"
def greeting():
    name = "tugba"

    def hello():    # bu fonks icin global scope bir üsttekidir yani tugbadır global string değil
        print("hello "+ name)
    hello()  # hello isimdeki fonks greeting içinde tanımla
greeting()



name = "global string"
def greeting():
    name = "tugba"

    def hello():    
        name = "deniz"
        print("hello "+ name)
    hello()  
greeting()




name = "global string"
def greeting():
    def hello():    
        print("hello "+ name)
    hello()  
greeting()

########################################

x = 50 
def test(x):
    print(f"x : {x}")
    x = 100
    print(f"changed x to {x}")
test(x) 
print(x)

x = 50 
def test():
    global x  # üstteki örnekle aynı sadece global keywordu var , dışardaki global x fonks içinden değiştirilir
    print(f"x : {x}")
    x = 100
    print(f"changed x to {x}")
test() 
print(x)  # üstte 50 burada 100 gelir çnk global x fonks içinde değişti, fonks içinde global old için dışardakini etkiliyor







