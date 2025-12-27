# %%
import numpy as np
from macholib.ptypes import sizeof

# Seviye 0 — Isınma (5-10 dk)
# 0.1 np.arange ile 0–19 arası sayıları üret.
# Shape: (20,)
# 0.2 Bu diziyi (4,5) matris yap.
# reshape kullan.
# 0.3 Matrisin:
# satırını,
# sütununu,
# Son 2 satırını
# ayrı ayrı al.
# 0.4 Matrisin tüm elemanlarını float’a çevir.


x = np.arange(20,).reshape((4,5))
x
x[1,2]
x[0,:]
x[:,2]
x[(2,3),:]
x[-2:,:]

x.dtype = float
x.dtype

# Seviye 1 — Temel işlemler + boolean indexing
# 1.1 a = np.array([3, 7, 2, 9, 1, 8])
# a içindeki tek sayıları seç.
# 1.2 a içindeki 5’ten büyükleri 100 yap (in-place).
# 1.3 b = np.arange(1, 11)
# b’nin karesini ve küpünü tek satırda üret (ayrı diziler).
# 1.4 x = np.array([1, 2, 3]), y = np.array([10, 20, 30])
# İki vektörün noktasal çarpımını (dot) hesapla.

a = np.array([3, 7, 2, 9, 1, 8])
z = a[np.mod(a,2)== 1]
z

a[a>5] = 100
a

b = np.arange(1,11)
karesi = np.power(b,2)
karesi
ucusu = np.power(b,3)
ucusu

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

x * y

# Seviye 2 — Broadcasting refleksi
# 2.1 M = np.arange(1, 13).reshape(3,4)
# Her satırın ortalamasını çıkar (sonuç shape (3,)).
M = np.arange(1, 13).reshape(3,4)
M
row_mean = np.mean(M,axis=1)

# Sonra her satırdan kendi ortalamasını çıkar (broadcast).

centered_mean = M - row_mean[:,None]
centered_mean

# 2.2 v = np.array([1, 10, 100, 1000])
# M’nin her sütununa v ekle.
v = np.array([1, 10, 100, 1000])
np.add(M,v)
# 2.3 (3,4) boyutlu bir matriste her elemana:
# satır indeksini + sütun indeksini ekle (ipucu: np.arange + reshape).
rows = np.arange(M.shape[0])[:, None]
rows
cols = np.arange(M.shape[1])[None,:]
cols

idx_added = M + rows + cols
idx_added


# Seviye 3 — Random + istatistik + eksen mantığı
# 3.1 np.random.seed(42) ile
# (1000,) boyutlu normal dağılım örnekle.
np.random.seed(42)
arr = np.random.normal(size=1000)
arr

# Ortalama, std, min, max hesapla.
arr.mean()
arr.std()
arr.min()
arr.max()
# 3.2 (200, 3) boyutlu “özellik matrisi” üret (uniform 0–1).
x = np.random.uniform(0,1,size=(200,3))
x
# Her sütunu 0-1 aralığında kalacak şekilde normalize et (min-max per column).
x_min = x.min(axis=0)
x_min
x_max = x.max(axis=0)
x_max
x_norm = (x - x_min) / (x_max -  x_min)
x_norm

# 3.3 Aynı matriste her satırın L2 normunu hesapla (shape (200,)).
np.linalg.norm(x_norm,axis=1)
x_norm


# Seviye 4 — Seçim, sıralama, arg* fonksiyonları
# 4.1 a = np.array([5, 1, 9, 2, 9, 3])
a = np.array([5,1,9,2,9,3])
max_value = a.max()
max_value
indices = np.where(a == max_value)
indices
# En büyük değerin indeks(ler)ini bul (tekrarlı maksimum var).
# 4.2 (10,10) matriste en büyük 5 elemanı bul:
# değerleri ve (row, col) indeksleriyle.
M = np.random.randint(0, 1000, size=(10,10))
k = 5
flat = M.ravel()
flat
top_flat_idx = np.argpartition(flat,-k)[-k::]
top_flat_idx
vas = flat[top_flat_idx]
vas
rows, cols = np.unravel_index(top_flat_idx, M.shape)


# 4.3 scores = np.random.randint(0, 101, size=50)
# İlk 10 en yüksek skoru (değer + indeks) getir (tam sıralama şart değil).
k=10
scores = np.random.randint(0, 101, size=50)

top_idx = np.argpartition(scores, -k)[-k::]
top_values = scores[top_idx]
top_values
order = np.argsort(top_values)[::-1]
top_idx_sorted = top_idx[order]
top_vals_sorted = scores[top_idx_sorted]



np.random.seed(42)
x = np.random.randint(0, 10, size=1000)

counts = np.bincount(x, minlength=10)
counts
counts[0]
counts[9] # 107
counts.sum()

np.random.seed(42)
A = np.random.rand(4, 3)
B = np.random.rand(5, 3)
A , B

diff = A[:, None, :] - B[None, :, :]
diff.shape

D = np.sqrt((diff**2).sum(axis=2))
D.shape

x = np.arange(20)
w = 5

windows = np.lib.stride_tricks.sliding_window_view(x, window_shape=w)
windows
windows.shape

