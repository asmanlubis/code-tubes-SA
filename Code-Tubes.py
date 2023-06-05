import itertools

# Fungsi untuk menghitung jarak antara dua titik
def hitung_jarak(titik1, titik2):
    x1, y1 = titik1
    x2, y2 = titik2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Implementasi metode Greedy
def greedy_rute_pengiriman_barang(lokasi_pusat, titik_tujuan):
    rute = [lokasi_pusat]
    while titik_tujuan:
        tujuan_terdekat = min(titik_tujuan, key=lambda x: hitung_jarak(rute[-1], x))
        rute.append(tujuan_terdekat)
        titik_tujuan.remove(tujuan_terdekat)
    return rute

# Implementasi metode Brute Force
def brute_force_rute_pengiriman_barang(lokasi_pusat, titik_tujuan):
    shortest_distance = float('inf')
    optimal_rute = None
    for perm in itertools.permutations(titik_tujuan):
        rute = [lokasi_pusat] + list(perm) + [lokasi_pusat]
        total_jarak = sum(hitung_jarak(rute[i], rute[i+1]) for i in range(len(rute)-1))
        if total_jarak < shortest_distance:
            shortest_distance = total_jarak
            optimal_rute = rute
    return optimal_rute

# Pengujian kode
lokasi_pusat = (0, 0)
titik_tujuan = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Menggunakan metode Greedy
rute_greedy = greedy_rute_pengiriman_barang(lokasi_pusat, titik_tujuan)
print("Rute dengan metode Greedy:", rute_greedy)

# Menggunakan metode Brute Force
rute_brute_force = brute_force_rute_pengiriman_barang(lokasi_pusat, titik_tujuan)
print("Rute dengan metode Brute Force:", rute_brute_force)
