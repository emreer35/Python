#%%
numbers = [4, 7, 1, 9, 2]
toplam = 0
for number in numbers:
    toplam += number
toplam

    

# %%
def kare_al(x):
    return x ** 2

kare_al(4)
# %%


# %% 

liste = [1,23,3.2,'yunus emre']
for l in liste:
    print(l)
# %%

type(liste)

# %%
len(liste)
# %%
del(liste)
# %%
liste
# %%
names = ['emre','yunus','er']
names[0] = 'yunus'
names[1] = 'emre'
names
# %%
names.append("yunus emre")
names
# %%
del names[len(names) - 1]
# %%
names
# %%
dir(names)
# %%
# append  klaiic eleman ekleme
names.append("sueda")
# %%
names
# %%
names.remove("er")
# %%
names
# %%
# listeye extend etme 
new_names_list = ['ali','veli','mehmet']
names.extend(new_names_list)
names
# %%
# insert denilen konuma isim eklemee 
# diger elemanlari kaydirir

names[1]
names.insert(1,"eklendi")
names[1]

# %%
# last indexe eleman ekleme
last_index = len(names)
names.insert(last_index,'last')
names
# %%
# pop index e gore eleman silme
names.pop(1)
# %%
names
# %%
# count kac adet oldugunu ogrenme 
names.count("emre")

# %%
names.index('sueda')
# %%


##################
# TUPLE
#################
# tuple () bu sekilde de olsuturulabilir 
# , koyarak ta olusturulabilir
new_tiple = tuple(['1',2,3,321,'321'])
new_tiple 
# %%
type(new_tiple)
# %%
new_tiple[1]
# %%
new_tiple.count("1")
# %%
new_tiple.index('1')
# %%


##################
# Dictionary
#################


ml_models = {
    "REG" : "Regresyon modeli",
    "LOJ" : "Lojistic Regresyon modeli"
}

copy_dict = ml_models.copy()
copy_dict
# %%
keys = ['price', 'amount','counter']
none_new_dict = ml_models.fromkeys(keys)
none_new_dict
# %%
ml_models
# %%
none_new_dict.get("price")
# %%

ml_models.items()
# %%
ml_models.keys()
# %%
ml_models.pop('LOJ')
# %%
ml_models
# %%
ml_models.popitem()
# %%
ml_models.setdefault('LOJ',"15555")
ml_models
# %%
ml_models.setdefault('LOJ',"2")

# %%

l = ['a',1,34,'asd','asd',2]

s = set(l)
s
# %%
t = (1,2,2,3,5,6,6,7,8)
ts = set(t)
ts
# %%
num1 = {1,2,3}
num2 = {2,3,4}
num1 - num2
num1.difference(num2) #yeni set oluşturur
# %%
num1.difference_update(num2)
a = {1,2,3,4,5,7,0}
b = {2,5,7,9}
a.difference_update(b)
# %%
a
# %%
b
# %%
