# TUPLE Data Structers

# Create a Tuple
# data type is Tuple


# tuple olusturma yontemleri 
# 1-
t = ("emre","ali","yusuf",1,2.2,[1,2,"3","fatih"])
# 2-
t = "emre","er",12,1,4.3,["1",2,3.5]


print(type(t))
# tuple eger 1 elemanli ise dikkat et 
t = ("emre") # bu bir stringtir 
type(t) # str 
print(type(t)) # str 

# fakat tuple olmasi icin , koymak yeterlidir 
t = ("emre",) # bu bir artik tuple dir 
print(type(t)) # tuple

# tuple lar da yine index ine gore secim yapabiliyoruz

tuple1 = ("emre","ali","yusuf",1,2.2,[1,2,"3","fatih"])
print(tuple1[0])

#tuple1[0] = "asu" # yapamyioruz cunku ekleme silme islemlerine destek vermiyor 
# print(dir(tuple))
# count 
count = tuple1.count("emre")
print(count)
# index
index = tuple1.index("emre")
print(index)
#%%
students = ("Emre","Ali","Emre","Ayse")
students.count("Emre")
students.index("Emre")

