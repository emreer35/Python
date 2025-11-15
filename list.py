# Listeler

# []
# list()

# notes = [70,80,90,40]
# type(notes) # list

# liste = [70, "asd", 19.3, "234"]
# type(liste) #list 

# list = [1,2,3,[1,2,3,4], "string", notes]

# print(len(list))

# print(type(list[0])) # burada list in ilk elemanin tipini goruruz

# twolist = [notes, liste]

# print(twolist[0][3]) # 0 inci index listinin 4. elemanina 
# # del(twolist) # listeyi sildik
# print(twolist)


# twolist[:2] # 2 ye kadar
# twolist[2:] # 2 den sona kadar





# Listelere eleman degistirme 
# 


liste = ["ali","veli","emre"]
liste[0] = "alinin_babasi" # indexin ismini degistirme
# print(liste)

liste[:2] = "alinin_babasi","velinin_babasi","emrenin_babasi" # isimlerini degistirme
# print(liste)

liste += ["kemal"] # listeye yeni eleman ekleme
# print(liste)

# del liste[0] # eleman silme islemi 
# print(liste)


print(dir(liste))
#'append',
#  'clear', icini tammaen temizler
#  'copy', copyalama yedek almak icin 
#  'count', sayisi
#  'extend', veriyi icerisine ekler dizi halinde degil ama 
#  'index', elemanin hangi indexte oldugunu ogrenme 
#  'insert', indexe gore eleman ekleme
#  'pop', indexe gore eleman silme  ve geri döndürür
#  'remove', yazdigimiz elemani silme 
#  'reverse', ters cevrme 
#  'sort' siralmaa

# append 
liste.append("artist") # listeye eleman ekledi kalici bir sekilde
print(liste)
#remove
liste.remove("artist") # listeden sectigimiz elemani sildi 
print(liste)
#extend
a = ["123",123]
liste.extend(a)
print(liste)
liste
#insert 
liste.insert(0,"emre")
liste

# listenin sonuna eleman ekleme 
lastIndex = len(liste)
liste.insert(lastIndex,"arkadas")
print(liste)

# pop indexe gore elaman silme

liste.pop(lastIndex-1)
print(liste)


# count 
# kac adet bundan var 
print(liste.count("arkadas"))

# copy 

list_yedek = liste.copy()
print(list_yedek)

# index 
print(liste.index("arkadas")) # 7. indexte
liste

liste


#%%
# list  practiceses

numbers = [1,4,6,8,5,4]
numbers.append(3)
numbers.count(4)
numbers.sort()
numbers.reverse()
numbers

numbers = [10,20,30,40,50]
numbers.insert(2,25)
numbers.pop(4)
numbers.remove(50)
numbers

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)

list3 = list1.copy()
list2.clear()
list3.count(3)
list1
list2
list3
# %%
shopping_list = ["ekmek","sut","peynir"]

new_item = input("Eklemek istediginiz urunu giriniz")
shopping_list.append(new_item)

deleted_item = input("silmek istediginiz urunun ismini giriniz") 
if deleted_item in shopping_list:
    shopping_list.remove(deleted_item)
    print(deleted_item, " urunu basariyla silindi")
else:
    print("urun bulunuamadi")

clear_list = input("Listenin hepsini silmek ister misini")
if clear_list.lower() == "e": 
    shopping_list.clear()
    print("urunler basariyla temizlendi")
elif clear_list.lower() =="h":
    print("silinmedi")



