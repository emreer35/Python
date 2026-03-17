# %%
salaries = [3000,8000,4000,5000,3000,2000,7000]
salaries.sort()

for salary in salaries:
    if salary == 3000:
        print("kesildi")
        break
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue # 3000 haric hepsini aldi 
    print(salary)


# 🎯 Mini Ödev 3
# 1’den 100’e kadar sayıları yazdır; sayı 37 olunca döngüyü break ile bitir.
# 1’den 50’ye kadar sadece 3’e bölünebilen sayıları yazdır (diğerlerini continue ile atla).

for i in range(1,101):
    if i == 37:
        break
    print(i)

for i in range(1,51):
    if i % 3 == 0 :
        print(i)


