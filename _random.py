import random

# result = random.random() # 0.0 - 1.0 sayı üretir
# result = random.uniform(54,85)  # iki sayi araasi sayi üretir
# result = random.randint(1,100) # int sayi üretir



# names = ["a", "b", "x"]
# result = names[random.randint(0,len(names)-1)] # index 0,1,2 gider ama 3 eleman var 3te hata olur
# # ya da
# result = random.choice(names)



liste = list(range(10))
random.shuffle(liste) # elemanlar sırali değil karışık gelir
result = liste 

liste = range(100)
result = random.sample(liste, 3) # belirtilen listeden istenilen sayi kadar elemani verir

print(result)