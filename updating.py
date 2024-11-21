# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())

# sayfa sonunda güncelleme
# with open("newfile.txt", "a", encoding="utf-8") as file:
#     file.write("\nCansu Ozturk")

# sayfa basinda güncelleme
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Ayse Ozturk\n" + content 
#     print(content)
# bu sekilde dosyaya aktarma olmaz boyle olur =>
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Ayse Ozturk\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# sf ortasında güncelleme
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     list = file.readlines()
#     list.insert(1, "Ali Veli\n")
#     file.seek(0)
#     for i in list:  # list elemanlatına tek tek for döngüsü ile ulaşırız
#         file.write(i)

# with open("newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())


with open("newfile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1, "Ayse Veli\n")
    file.seek(0)
    file.writelines(list) # for döngüsü yerine tek tek dolasma

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())