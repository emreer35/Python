
# %%
class VeriBilimci():
    title = ''
    sql = 'evet'
    bildigi_diller = ['sql']

VeriBilimci.sql
VeriBilimci.sql = 'hayir'
VeriBilimci.sql


# Sinif orneklendirmesi (instantiation)

ali = VeriBilimci()
ali.sql
ali.bildigi_diller.append('python')
ali.bildigi_diller

veli = VeriBilimci()

veli.sql


# %%
# Ornek Ozellikleri

class VeriBilimci():
    title = ''
    sql = 'evet'
    bildigi_diller = ['R','Python'] # bu sekilde veribilimciye
    # otomatik dil atayabiliyorum
    def __init__(self): # burada ise her nesnenin farkli bir dli olabilir 
        self.bildigi_diller = []
berk = VeriBilimci()
berk.bildigi_diller.append('python')
berk.bildigi_diller

daisy = VeriBilimci()
daisy.bildigi_diller.append('R')
daisy.bildigi_diller
daisy.sql

VeriBilimci.bildigi_diller



# %%

class VeriBilimci():
    title = ''
    sql = 'evet'
    bolum = ''
    bildigi_diller = ['R','Python'] 
    def __init__(self): 
        self.bildigi_diller = []
        self.bolum = ''

berk = VeriBilimci()
berk.bolum = 'polsilik'
berk.bolum
VeriBilimci.bolum
ali = VeriBilimci()
ali.bolum = 'istatistik'
ali.bolum
# %%

class VeriBilimci():
    calisanlar = []
    def __init__(self): 
        self.bildigi_diller = []
        self.bolum = ''
    def add_language(self, new_language):
        self.bildigi_diller.append(new_language)

dir(VeriBilimci)
ali = VeriBilimci()
VeriBilimci.add_language(ali,'python')
ali.bildigi_diller
ali.add_language('r')
ali.bildigi_diller

