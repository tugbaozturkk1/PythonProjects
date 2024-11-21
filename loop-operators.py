# loop=döngü
# range, enumerate, zip metotları 
# for item in range(10):
#     print(item)              # range liste olusturur
# for item in range(50,100,10):
#     print(item)

# print(list(range(5,10,2)))   

# # enumerate
# index=0
# greeting="Hello there"
# for letter in greeting:
#     print(f"index: {index} letter: {letter}")
#     index+=1

# greeting="Hello"
# for item in enumerate(greeting):
#     print(item)



# zip
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
print(list(zip(list1,list2)))
for item in zip(list1,list2):
    print(item)