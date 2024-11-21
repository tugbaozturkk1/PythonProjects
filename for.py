# numbers=[1, 2, 3, 4, 5]
# # for num in numbers:
# #     print(num)       # listeden tek tek elemanları al num içine at 
# for t in numbers:
#     print("tugba")

# names = ["tugba", "deniz"]
# for name in names:
#     print(f"my name is {name}")

# name = "Deniz"
# for n in name:
#     print(n)    # string ifadenin her bir harfi liste elemanı olarak algılanır

# tuple=(1,2,3,4,5)
# for t in tuple:
#     print(t)

# tuple1 = [(1,2),(3,5)]
# for a in tuple1:
#     print(a)

# for a,b in tuple1:
#     print(a,b)

# for a,b in tuple1:
#     print(b)

d = {"k1":1, "k2":2}  # dictionary {"key","value"} idi
for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(key, value)

for key,value in d.items():
    print(key)

for key,value in d.items():
    print(value)