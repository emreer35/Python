# %%
# while

number = 1

while number <10:
    number+= 1
    print(number)


# while kullanarak 1’den 10’a kadar sayıları yazdır.
# Kullanıcı 0 girene kadar sayı iste, her sayıyı toplayıp en sonunda toplamı yazdır.
# Kullanıcıdan şifre iste, doğru şifreyi bilene kadar sormaya devam et.
#  (şifreyi kodun içine string olarak yaz)

number = 1
while number <= 10:
    print(number)
    number += 1

sayi = int(input("Bir sayi giriniz"))
toplam = 0
while sayi != 0 :
    toplam += sayi
    sayi = int(input("tekrar sayi gir"))
toplam


password = input("sifrenizi giriniz lutfen")

while password != "123456":
    password = input("sifrenizi tekrar giriniz")
else:
    print("sifreniz dogru")

