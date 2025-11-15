#%%
print
# ?print


def kare_al(x):
    return x**2

print(kare_al(3))

def kare_al(x):
    print(f"girilen sayi: {x} sayinin karesi: {x**2}")

kare_al(3)


def self_introduction(name):
    print(f"Merhaba benim adim {name}")

self_introduction('emre')


def impact(x,y):
    print(f'girilen sayilar: {x} {y} carpimi: {x*y}')
impact(3,5)

def impact(x,y = 1):
    print(x*y)
impact(3)
impact(3,5)

# Esnek parametreler: *args, **kwargs

# args tuple
# kwargs dict

def sum_all_numbers(*arg):
    return sum(arg)
sum_all_numbers(1,2,3,4,5,6,7,8,9,11,111,112) 

def show_settings(**kwargs):
    return kwargs
show_settings(boy=179, kilo = 70)
# %%
# burada section i ismiyle belirtmemiz gerekiyor 
def explain(x,y,/,name,*,section):
    result = x*y
    return f"Bolum: {section} Carpimi yapan kisi: {name} Carpim: {result}"
explain(1,2,"emre",section="toplama cikarma carpma")
explain(1,2,name="emre",section="toplama cikarma carpma")


# return islmeini tuple ile yapar 

def sum(a,b):
    result = a + b
    return result, None

result, error = sum(3,5)
result, error