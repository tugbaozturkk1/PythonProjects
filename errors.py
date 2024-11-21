# error handling => hata yönetimi

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ValueError, ZeroDivisionError) as wrong:
#     print("yanlis bilgi girdin")
#     print(wrong)
# else:  # exceptten gelen else
#     print("all informations are true")

while True: 
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as wrong:  # exception yazarak bütün hatalar dahil edilmis olur
        print("yanlis bilgi girdin")
        print(wrong)  # dogru bilgi girene kadar döngü calisir
    else:  # exceptten gelen else
        break











