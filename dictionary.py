#%%
# Dictioary Data Types
# 1- Kapsayicidir
# 2- Sirasizdir
# 3- Degistirebilir

# Dictionary {"key":"value"} seklinde olusturulur

dict = {"REG": "Regrasyon Modeli",
        "LOJ" : "Lojistic Regrasyon Modeli",
        "CART" : "Classification and Reg"}
# print(type(dict)) # type dict dir

# print(dict)

methods = dir(dict)
# print(methods)
#  'clear', iceriginin hepsini siler
#  'copy', bir dict i kopyalar
#  'fromkeys', anahtarlari verip her anahtara ayni degeri atar (key, "value")
#  'get',  anahtara karşılık gelen değeri döndürür, anahtar yoksa hata vermez (None döner)
#  'items',
#  'keys', Sözlüğün tüm anahtarlarını döndürür.
#  'pop', Verilen anahtarı siler ve onun değerini geri döndürür.
#  'popitem', Sözlüğe en son eklenen öğeyi siler ve (key, value) olarak döndürür.
#  'setdefault', Bir anahtar varsa değerini döndürür, yoksa ekler ve varsayılan değer atar.
#  'update', Birden fazla değeri aynı anda günceller veya ekler.
#  'values' Sözlüğün sadece değerlerini döndürür.

# len = len(dict)
# print(len) # 3

dict1 = {"REG": ["Reg",1,3.3],
        "LOJ" : ["Lojistic Regrasyon Modeli", 12.2,"33"],
        "CART" : ["Classification and Reg", 123,"emre", dict]}

dict1["CART"][3]["REG"]

# print(dict1)

# print(dict1["CART"])

# print(dict1["CART"]["REG"])

# dict1.get()

# Dict veri ekleme 
dict1["GBM"] = "Gradient Boosting Machine"
dict1

dict1["REG"] = "Coklu regrasyon modeli"
dict1


#  'clear', iceriginin hepsini siler
# dict1.clear()
dict1


#  'copy', bir dict i kopyalar
copyDect1 = dict1.copy()
copyDect1


#  'fromkeys', anahtarlari verip her anahtara ayni degeri atar (key, "value")
keys = ["price", "number", "counter"]
none_new_dict = dict.fromkeys(keys) # bos oldugundan none degerini verdi
none_new_dict
new_dict = dict.fromkeys(keys,155)
new_dict


#  'get',  anahtara karşılık gelen değeri döndürür, anahtar yoksa hata vermez (None döner)
new_dict.get("price") # 155


#  'items', key value degeri seklinde deger donderir
dict1.items() # array seklinde key value degerini donderir 


#  'keys', Sözlüğün tüm anahtarlarını döndürür.
dict1.keys() # array seklinde keyleri dondurur


#  'pop', Verilen anahtarı siler ve onun değerini geri döndürür.
dict1.pop("CART") # siler ve silinen degeri geri donderdi

#  'popitem', Sözlüğe en son eklenen öğeyi siler ve (key, value) olarak döndürür.
dict1.popitem() # son eklenen degeri sildi ve silinen degeri keyvalue dondurdu


#  'setdefault', Bir anahtar varsa değerini döndürür, yoksa ekler ve varsayılan değer atar.
dict1.setdefault("CPR", 15000) # yoksa degeri atar 
dict1
dict1.setdefault("LOJ","emre") # egerki anahtar varsa degeri donderrir 
dict1


#  'update', Birden fazla değeri aynı anda günceller veya ekler.
dict1.update({"CPR" : "CPRRINNNGG", "LOJ": "Lojistic Regrasyon Modeli"})
dict1

dict1.update({"emre": "emre"}) # suslu paranteze almayi unutma
dict1


#  'values' Sözlüğün sadece değerlerini döndürür.
dict1.values() # array seklinde value degerlerini donderir

# del methods



# %%

# dictinary sozlugu exercises

book = {"title" : "bir kucucuk osmancik vardi", "author": "osmancik", "year" : 2012, "page": 238}
# odev 1
book["title"]
book['year']
# odev 2
book.update({"genre" : "Roman"})
print(book.pop("page"))
book.get("publisher")
#odev 3
for key, value in book.items():
    print(key ,":", value)

#odev4
library = {
    "A1": {"title": "1984", "author": "Orwell"},
    "A2": {"title": "Dune", "author": "Herbert"}
}

library.setdefault("A3",{"title": "Sefiller", "author": "Hugo", "year": 1862})

library
keys = ["B1","B2", "B3"]
new_books = dict.fromkeys(keys,"empty")


