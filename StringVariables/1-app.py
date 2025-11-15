#String degerler 
#yorum satiri "#" bu sekilde alinir

type(123)
'a' + 'a' # 2 a yi yan yana koyar
#'a' - 'a' # burada hata firlatir cunku string ifadelerde cikarma yapilamaz
"a"*3 # hata vermez 3 a yazdirir
#'a' / 'a' # burada hata firlatir cunku string ifadelerde bolme yapilamaz

 # string methods - len() - the len method's give a string method's len

str = "yunus emre er"
print(str)
# del str
print(str)

a = len(str)
print(a)


print(str.upper()) # buyuk harfe cevirme 

print(str.lower()) # kucuk harfe cevirme

upperrCapitalize = str.upper()

print(upperrCapitalize.islower()) # false 
print(upperrCapitalize.isupper()) # true

# string methods - replace() 

replace = str.replace("u","a") # u harflerini a ya cevirir
print(replace)

# string methods - strip() -- onundeki ve arkasinda ki bos degerleri alir
# whiteSpace = "*  yunus emre er.       "
print(str.strip())
# print(whiteSpace.strip()) # burada bosluklari kaldirir
# print(whiteSpace.strip("*")) # burada * degerini kaldirir


# string methods find methods  dir()
# print(dir(str))

a = str.capitalize()
print(a)

a = str.count("y")
print(a)

a = str.title()
print(a)

# stringler methods substrings - istedigimiz kadarini alma 

a = str[0:3] # sol dahil sag a kadar 
print(a) # yun 


