# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı")
#     file.close()

# file = open("newfile.txt", "r", encoding = "utf-8")
# for i in file: # bos satirla vermemesi için end ile bosluk eklersin
#     print(i, end="")

# file.close()


# file = open("newfile.txt", "r", encoding = "utf-8")
# content1 = file.read()
# print("icerik 1")
# print(content1)
# content2=file.read()   # read bütün içeriği okur 2ye gelince kürsör sonda kaldıgı icin okuyacak bir sey kalmaz bosluk gösterir
# print("icerik 2") 
# print(content2)
# file.close()

# file = open("newfile.txt", "r", encoding = "utf-8")
# content = file.read(5) # ilk 5 karakteri okur
# print(content)

# readline() fonks = hep 1 satır okur
# file = open("newfile.txt", "r", encoding = "utf-8")
# print(file.readline(), end="")
# print(file.readline(), end="")
# file.close()

# readlines() fonks
file = open("newfile.txt", "r", encoding = "utf-8")
liste = file.readlines()
print(liste)
file.close()