# list = [1, 2, 3]
# tuple = (1, "iki", 3)
# print(type(list))
# print(type(tuple))
# print(tuple[2])

tuple = ("tugba", "tugce", "tugce")
print(tuple.count("tugce"))   # kaç tane oldugunu yazar
print(tuple.index("tugba"))   # nerede oldugunu söyler hangi indexte
names = ("eylül", "rabia") + tuple
print(names)