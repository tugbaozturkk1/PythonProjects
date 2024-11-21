with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read(10))
    file.seek(0) # kürsörü yazdıgın konuma gönderir
    print(file.tell()) # tell kürsörün konumunu verir
    print(file.read()) # kürsör en sonda gelecek bilgi kalmadı bosluk verir
# file.close grek kalmaz
