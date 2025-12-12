
# %%
# True False gosterimi
sinir = 5000

sinir == 4000 # false



# %%

sinir = 50000

gelir = 40000

if gelir < sinir: 
    print(f"{gelir} {sinir} degerinden dusuktur ")
else:
    print(f"{gelir} {sinir} degerinden buyuktur")

# %%
sinir = 50000

gelir = 40000
if gelir < sinir:
    print(f"{gelir} {sinir} degerinden dusuktur ")
elif gelir > sinir:
    print(f"{gelir} {sinir} degerinden buyuktur")
else: 
    print("deger esittir")

# example 

sinir = 50000
company_name = input("Magaza adini giriniz")
gelir = int(input("Magaza gelirini giriniz"))

listofCompaniesSalary = {}
listofCompaniesSalary.update({"Company Name": company_name, "Salary": gelir})


if gelir > sinir:
    print(f"gelir: {gelir} \n {company_name} magazasinin geliri sinirdan buyuktur")
elif gelir < sinir:
    print(f"gelir: {gelir} \n {company_name} magazasinin geliri sinirdan kucuktur")
else:
    print(f"gelir: {gelir} \n {company_name} magazasinin geliri sinirina esittir")

listofCompaniesSalary
# %%
