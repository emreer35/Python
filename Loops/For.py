

#for 
# %% 
students = ['ali','emre','veli','riza']

for student in students:
    print(student)
# %%
# loop and function
# maaslara %20 zamn getirecek kodu yaz

salaries = [1000,2000,3000,4000,5000]

def raise_salary(x):
    return x*120/100

for salary in salaries:
    new_salary = raise_salary(salary)
    print(f"new salary: {new_salary}")


# %%
# Loop, Function and if Else

# maasi 3000 den buyuk olana %10 , az olanlara %20 zam
salaries = [1000,2000,3000,4000,5000]
def raise_salary_less_than(x):
    return x*120/100
def raise_salary_grather_than(x):
    return x*110/100

for salary in salaries:
    if salary >= 3000:
        new_salary = raise_salary_grather_than(salary)
    else:
        new_salary = raise_salary_less_than(salary)
    print(new_salary)

# %%

for i in range(1,5):
    print(i)
# for i in range(5): → “0’dan 5’e kadar (5 hariç) sırayla değerleri i’ye ver”
# i bir değişken adı – x, index, sayi ne istersen yazabilirsin.
# range(5) → 0, 1, 2, 3, 4 üreten bir sıra (iterable).

# range(stop)              # 0, 1, 2, ..., stop-1
# range(start, stop)       # start, start+1, ..., stop-1
# range(start, stop, step) # step adımlarla ilerler

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(10, 1, -1):
    print(i)

kelime = "dongu"

for harf in kelime:
    print(harf)


numbers = [1,2,3,4,5,6]

for number in numbers:
    print(f"{number} : {number**2}")


# %%

# Kendin dene (yaz, çalıştır):
# 1’den 20’ye kadar çift sayıları yazdır.
# Bir isimler listesi oluştur; her ismi "Merhaba, <isim>" şeklinde yazdır.
# Kullanıcıdan 5 sayı al, hepsini bir listede topla ve en sonunda listeyi yazdır.

for i in range(1,20,2):
    print(i)

names = ['emre','ali','berk','ibrahim','galip']
for name in names:
    print(name)

numbers = []
for get_number in range(1,6):
    number = int(input(f"Lutfen {get_number}. sayiyi giriniz"))
    numbers.append(number)

for number in numbers:
    print(number)
numbers = [int(input(f"{i}. sayı: ")) for i in range(1, 6)]
print(numbers)


# %%
# 1’den 50’ye kadar 3’e bölünen sayıların küplerini bir liste comprehension ile üret.
# isimler = ["ali", "ayşe", "mehmet"] listesinden, bütün isimleri büyük harfe çeviren bir list comprehension yaz.
# 1’den 10’a kadar sayıları anahtar, karelerini değer yapan bir sözlük (dict) comprehension yaz

cupe = [i **3 for i in range(1,50) if i % 3 == 0]
cupe

isimler = ["ali","ayse","mehmet"]
to_upper_names = [i.upper() for i in isimler]

square_numbers = {i: i**2 for i in range(1,10)}
square_numbers


for i in range(1,6):
    for j in range(1,6):
        print(f"{i} x {j} = {i*j}")


matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
    print()

# 1’den 10’a kadar olan sayılar için çarpım tablosu yap (1x1=1 formatında).
# * karakteriyle şöyle bir üçgen çiz:
# *
# **
# ***
# ****
# *****
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")

for i in range(1,6 ):
    for j in range(1,i+1):
        print("*", end="")
    print()

for i in range(6,1,0-1):
    print('*' * i)
    
