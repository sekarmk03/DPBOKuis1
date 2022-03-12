'''
Saya Sekar Madu Kusumawardani_2007703 mengerjakan Kuis 1 dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

# mengimport semua kelas
from Petani import Petani
from PemilikTengkulak import PemilikTengkulak
from MarketPlace import MarketPlace
from Lahan import Lahan
from KomoditasPertanian import KomoditasPertanian

# membuat list untuk menampung objek
petani = []
pemilikTengkulak = []
marketPlace = []
lahan = []
komoditasPertanian = []


# MEMASUKKAN DATA HARDCODE
# PETANI
# setiap petani adalah objek penduduk juga
# Petani 1
pt = Petani()
pt.setIdPenduduk("Pd_123")
pt.setNama("Dadang")
pt.setAlamat("Karawang")
pt.setIdPetani("Pt#123")
pt.setStatus("Pemilik")
petani.append(pt)

# Petani 2
pt = Petani()
pt.setIdPenduduk("Pd_456")
pt.setNama("Asep")
pt.setAlamat("Pandeglang")
pt.setIdPetani("Pt#456")
pt.setStatus("Pemilik")
petani.append(pt)

# Petani 3
pt = Petani()
pt.setIdPenduduk("Pd_789")
pt.setNama("Ujang")
pt.setAlamat("Bekasi")
pt.setIdPetani("Pt#789")
pt.setStatus("Buruh")
petani.append(pt)

# PEMILIK TENGKULAK
# setiap pemilik tengkulak adalah objek penduduk juga
# Pemilik Tengkulak 1
tk = PemilikTengkulak()
tk.setIdPenduduk("Pd_1011")
tk.setNama("Dodi")
tk.setAlamat("Depok")
tk.setIdTengkulak("Tk^123")
pemilikTengkulak.append(tk)

# Pemilik Tengkulak 2
tk = PemilikTengkulak()
tk.setIdPenduduk("Pd_1213")
tk.setNama("Kiwil")
tk.setAlamat("Bandung")
tk.setIdTengkulak("Tk^456")
pemilikTengkulak.append(tk)

# MARKETPLACE
# MarketPlace 1
mp = MarketPlace(idMarketPlace="Mp-123", namaMarketPlace="DuperMarket",
sistemMarket="Offline", tipeMarket="Business to Business")
marketPlace.append(mp)

# MarketPlace 2
mp = MarketPlace(idMarketPlace="Mp-456", namaMarketPlace="Amanah Sayur",
sistemMarket="Offline", tipeMarket="Business to Customer")
marketPlace.append(mp)

# MarketPlace 3
mp = MarketPlace(idMarketPlace="Mp-789", namaMarketPlace="TokoPaEdi",
sistemMarket="Online", tipeMarket="Business to Business")
marketPlace.append(mp)

# LAHAN
# Lahan 1
lh = Lahan(idLahan="Lh_1", jenisTanah="Sawah", sistemTanam="Tunggal Tanam", desa="Duren",
kecamatan="Klari", kota="Karawang", provinsi="Jawa Barat", luas=31)
lahan.append(lh)
# menambahkan lahan ke objek petani
petani[0].setLahan(lahan[0])

# Lahan 2
lh = Lahan(idLahan="Lh_2", jenisTanah="Gembur", sistemTanam="Campur Sari", desa="Anggadita",
kecamatan="Klari", kota="Karawang", provinsi="Jawa Barat", luas=23)
lahan.append(lh)
# menambahkan lahan ke objek petani
petani[1].setLahan(lahan[1])

# Lahan 3
lh = Lahan(idLahan="Lh_3", jenisTanah="Gambut", sistemTanam="Campur Sari", desa="Cibalongsari",
kecamatan="Klari", kota="Karawang", provinsi="Jawa Barat", luas=19)
lahan.append(lh)
# menambahkan lahan ke objek petani
petani[1].setLahan(lahan[2])

# Lahan 4
lh = Lahan(idLahan="Lh_4", jenisTanah="Gambut", sistemTanam="Tunggal Tanam", desa="Hegarmanah",
kecamatan="Cidadap", kota="Bandung", provinsi="Jawa Barat", luas=8)
lahan.append(lh)
# menambahkan lahan ke objek petani
petani[2].setLahan(lahan[3])

# KOMODITAS
# Komoditas 1
kp = KomoditasPertanian(idKomoditas="K0m0-01", namaKomoditas="Padi", lahan=lahan[0],
dijual=("Tengkulak " + pemilikTengkulak[0].getNama()))
komoditasPertanian.append(kp)
# menambahkan komoditas ke objek lahan dan objek pemilik tengkulak
lahan[0].setKomoditas(komoditasPertanian[0])
pemilikTengkulak[0].setKomoditas(komoditasPertanian[0])

# Komoditas 2
kp = KomoditasPertanian(idKomoditas="K0m0-02", namaKomoditas="Singkong", lahan=lahan[1],
dijual=("Tengkulak " + pemilikTengkulak[0].getNama()))
komoditasPertanian.append(kp)
# menambahkan komoditas ke objek lahan dan objek pemilik tengkulak
lahan[1].setKomoditas(komoditasPertanian[1])
pemilikTengkulak[0].setKomoditas(komoditasPertanian[1])

# Komoditas 3
kp = KomoditasPertanian(idKomoditas="K0m0-03", namaKomoditas="Ubi Jalar", lahan=lahan[1],
dijual=("Tengkulak " + pemilikTengkulak[1].getNama()))
komoditasPertanian.append(kp)
# menambahkan komoditas ke objek lahan dan objek pemilik tengkulak
lahan[1].setKomoditas(komoditasPertanian[2])
pemilikTengkulak[1].setKomoditas(komoditasPertanian[2])

# Komoditas 4
kp = KomoditasPertanian(idKomoditas="K0m0-04", namaKomoditas="Singkong", lahan=lahan[2],
dijual=("MarketPlace " + marketPlace[0].getNamaMarketPlace()))
komoditasPertanian.append(kp)
# menambahkan komoditas ke objek lahan dan objek marketplace
lahan[2].setKomoditas(komoditasPertanian[3])
marketPlace[0].setKomoditas(komoditasPertanian[3])

# Komoditas 5
kp = KomoditasPertanian(idKomoditas="K0m0-05", namaKomoditas="Jagung", lahan=lahan[3],
dijual=("MarketPlace " + marketPlace[1].getNamaMarketPlace()))
komoditasPertanian.append(kp)
# menambahkan komoditas ke objek lahan dan objek marketplace
lahan[3].setKomoditas(komoditasPertanian[4])
marketPlace[1].setKomoditas(komoditasPertanian[4])

# Komoditas 6
kp = KomoditasPertanian(idKomoditas="K0m0-06", namaKomoditas="Gandum", lahan=lahan[2],
dijual=("MarketPlace " + marketPlace[2].getNamaMarketPlace()))
komoditasPertanian.append(kp)
# menambahkan komoditas ke objek lahan dan objek marketplace
lahan[2].setKomoditas(komoditasPertanian[5])
marketPlace[2].setKomoditas(komoditasPertanian[5])


# OUTPUT
# DATA PETANI
print("--------- DATA PETANI ---------")
no = 1
for p in petani:
    print("*" + str(no))
    p.printPetani()
    no+=1

print("")

print("Pilih data yang ingin ditampilkan")
print("1. Data Pemilik Tengkulak")
print("2. Data MarketPlace")
print("3. Data Komoditas")
print("4. Data Lahan")
choose = int(input("> "))

if choose == 1:
    # DATA PEMILIK TENGKULAK
    print("--------- DATA PEMILIK TENGKULAK ---------")
    no = 1
    for pt in pemilikTengkulak:
        print("^" + str(no))
        pt.printTengkulak()
        no+=1
    print("")
elif choose == 2:
    # DATA MARKETPLACE
    print("--------- DATA MARKETPLACE ---------")
    no = 1
    for mp in marketPlace:
        print("@" + str(no))
        mp.printMarketPlace()
        no+=1
    print("")
elif choose == 3:
    # DATA KOMODITAS
    print("--------- DATA KOMODITAS ---------")
    no = 1
    for km in komoditasPertanian:
        print("#" + str(no))
        km.printKomoditas2()
        no+=1
    print("")
elif choose == 4:
# DATA LAHAN
    print("--------- DATA LAHAN ---------")
    no = 1
    for lh in lahan:
        print("~" + str(no))
        lh.printLahan()
        no+=1
    print("")
else:
    print("Pilihan tidak tersedia.")