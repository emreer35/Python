# SET 

# 1- Sirasizdir
# 2- Degerleri essizdir
# 3- Degistirilebilir
# 4- Farkli tipler barindirir

# Set Olusturma 
# %%
# s = set()
# s
sets = {1,2,3,3,3,3}

# set leri diger veri tiplerinden donsuturebiliriz
# 1- List
li = ["a",1,3.5,"cherry"]
setlist = set(li)

# 2- tuple
t = (1,2,3,'a','b',3.52)
settuple = set(t)

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)
setstring = set(ali)
type(setstring)
setstring # her bir harfi tek tek yazdirdi 1 kere yazdi 
# parcalayarak tek elemanli yani char gibi yazdi 

li[0]
settuple[0] #'set' object is not subscriptable

dir(setstring)
# Set Metodlari 
#  'add',  Kümeye yeni bir eleman ekler.
#  'clear', set i tamamen siler 
#  'copy', kopyalar
#  'difference', bir kumede olup digerinde olmayan ifadeyi getirir
#  'difference_update',
#  'discard',
#  'intersection',
#  'intersection_update',
#  'isdisjoint',
#  'issubset',
#  'issuperset',
#  'pop',
#  'remove', silme islemini yapar
#  'symmetric_difference',
#  'symmetric_difference_update',
#  'union',
#  'update'

# %%

# ADD
#  set veri yapisina ekleme yapar sirasizdir!!!
# Kümeye yeni bir eleman ekler.
l = ["ali",'veli'] 
s = set(l)
s.add('emre')
s.add('emre')
s.add('burasi_cok')
s.add("kotu_bir_yer")

# CLEAR
# Kümeyi tamamen temizler.
# s.clear()

# COPY
# Kopyasını oluşturur.
s_copy = s.copy()
s_copy

# REMOVE
# silme islemini yapar deger dondermez 
s.remove("emre")
# print(s.remove("emre"))  none 

# DISCARD
#  remove ile ayni gorevi yapar fakat hata donmez
s.discard("emre")

# DIFFERENCE ( - ifadesi ile de yapiliyor )
# İki küme arasındaki farkı döndürür (yeni set oluşturur).
# a kumesinde olup b kumesinde olmayan
num1 = {1,2,3}
num2 = {2,3,4}
num1 - num2
num1.difference(num2) #yeni set oluşturur

# Difference_update()
# a kümesinden b kümesindeki ortak elemanları KALICI olarak çıkarır.
num1.difference_update(num2)
a = {1,2,3,4,5,7,0}
b = {2,5,7,9}
a.difference_update(b)

# Intersection ( & ifadesi ile de yapilir )
# Kümelerin kesişimini (ortak elemanlarını) döndürür.
a.intersection(b) # 2,5,7

a & b


# intersection_update
# Kesişimi kalıcı hale getirir.
a.intersection_update(b) # a kumesini direkt bu hale getiriyor 

# Isdisjoint
# Hic ortak elemani yok mu diye bakar 
# True ya da False doner

a.isdisjoint(b)  # false dondu yani ortak elemani var

# Issubset()
# bir kume diger kumenin alt kumesi mi ona bakar
a = {1,2,3}
b = {1,2}
b.issubset(a) # true ya da false doner 

# Issuperset
# Bir küme, diğerinin üst kümesi mi?
a = {1,2,3,4,5}
b = {1,2,3}
a.issuperset(b) # true ya da false doner

# Pop 
# Set ler sirasiz oldugu icin rastgele bir tanesini siler ve
# sildigi degeri donerir

a.pop() # mesela icerisinden 1 i sildi

# symmetric_diffrence()
# ki kümede olup kesişimde olmayan elemanları döndürür (A∪B - A∩B).
# yani a ile b yi birlestir farkini cikar 
a = {1,2,3,4,5}
b = {1,2,3}
a.symmetric_difference(b) # 4,5

# symmetric_difference_update()
# yukarida ki islemin kalici halini yapar
a.symmetric_difference_update(b) # a artik 4,5 olur 

# Union 
# İki kümenin birleşimini döndürür (A ∪ B).
# iki kumeyi birlestirir 

a.union(b)

# Update 
# Birleşimi kalıcı hale getirir.

a.update(b)