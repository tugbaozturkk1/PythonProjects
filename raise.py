# raising an exception = hata oluşturma
def checkPassword(psw):
    import re
    if len(psw) < 5:
        raise Exception("parola en az 6 karakterli olacak")
    elif not re.search("[a-z]", psw): # not var küçük harf yoksa parolada hata verir
        raise Exception("parola küçük harf icermeli")
    elif not re.search("[A-Z]", psw):
        raise Exception("büyük harf gerek")
    elif not re.search("[0-9]", psw):
        raise Exception("rakam gerek")
    elif not re.search("[_@]", psw):
        raise Exception("alphanumeric karakter gerek")
    elif re.search(" ", psw):
        raise Exception("password should not have spaces ")
    else:
        print("gecerli parola")


password = "123456Aa_"
try:
    checkPassword(password)
except Exception as wrong:
    print(wrong)    
else:
    print("geçerli olan parola")
finally:
    print("doğrulama okay")