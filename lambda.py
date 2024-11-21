# def square(num):    # kare alma fonks.
#     return num ** 2
# numbers=[1,3,5,9]

# result = list(map(square, numbers))

# print(result)
#                                              # ikiside aynı sonuca gider


# for item in map(square, numbers):
#     print(item)



# lambda expressions = ismi olmayan fonks. tanımlamak için
# numbers = [1,3,5,9]
# result = list(map(lambda num: num ** 2 , numbers))
# print(result)


# a = lambda num: num ** 3
# result = a(2)
# print(result)



square = lambda num: num ** 2
numbers = [1,3,5,9,10,4]
def check_even(num):
    return num%2==0
print(list(filter(check_even, numbers)))

                                            # ikisi de aynı şey

square = lambda num: num ** 2
numbers = [1,3,5,9,10,4]
def check_even(num):
    return num%2==0
print(list(filter(lambda num: num%2==0, numbers)))



a = lambda num: num%2==0
result = a(numbers[4])   # 4.index=10 çift old için true değer verir
print(result)



