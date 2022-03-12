'''
Saya Sekar Madu Kusumawardani_2007703 mengerjakan Kuis 1 dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

class Lahan: # lahan bisa dibuat tanpa komoditas (asumsi lahan kosong)
    # atribut private
    __idLahan = ""
    __jenisTanah = ""
    __sistemTanam = ""
    __desa = ""
    __kecamatan = ""
    __kota = ""
    __provinsi = ""
    __luas = 0
    __komoditas = [] # banyak komoditas dalam 1 lahan, diisi setelah komoditas ada

    def __init__(self):
        # constructor
        self.__idLahan = ""
        self.__jenisTanah = ""
        self.__sistemTanam = ""
        self.__desa = ""
        self.__kecamatan = ""
        self.__kota = ""
        self.__provinsi = ""
        self.__luas = 0
        self.__komoditas = [] # diisi setelah objek komoditas dibuat
        
    def __init__(self, idLahan, jenisTanah, sistemTanam, desa, kecamatan, kota, provinsi, luas):
        # constructor
        self.__idLahan = idLahan
        self.__jenisTanah = jenisTanah
        self.__sistemTanam = sistemTanam
        self.__desa = desa
        self.__kecamatan = kecamatan
        self.__kota = kota
        self.__provinsi = provinsi
        self.__luas = luas
        self.__komoditas = [] # diisi setelah objek komoditas dibuat
        
    # method get set atribut
    def setIdLahan(self, idLahan):
        self.__idLahan = idLahan

    def getIdLahan(self):
        return self.__idLahan

    def setJenisTanah(self, jenisTanah):
        self.__jenisTanah = jenisTanah

    def getJenisTanah(self):
        return self.__jenisTanah

    def setSistemTanam(self, sistemTanam):
        self.__sistemTanam = sistemTanam

    def getSistemTanam(self):
        return self.__sistemTanam

    def setDesa(self, desa):
        self.__desa = desa

    def getDesa(self):
        return self.__desa

    def setKecamatan(self, kecamatan):
        self.__kecamatan = kecamatan

    def getKecamatan(self):
        return self.__kecamatan

    def setKota(self, kota):
        self.__kota = kota

    def getKota(self):
        return self.__kota

    def setProvinsi(self, provinsi):
        self.__provinsi = provinsi

    def getProvinsi(self):
        return self.__provinsi

    def setLuas(self, luas):
        self.__luas = luas

    def getLuas(self):
        return self.__luas

    def setKomoditas(self, komoditas): # menambah objek Komoditas
        self.__komoditas.append(komoditas)

    def getKomoditas(self):
        return self.__komoditas

    # method cetak data
    def printLahan(self):
        print("> Lahan " + self.getIdLahan())
        print("  Jenis Tanah\t: " + self.getJenisTanah())
        print("  Sistem Tanam\t: " + self.getSistemTanam())
        print("  Alamat\t: Ds. " + self.getDesa() + ", Kec. " + self.getKecamatan() +
                ", Kota " + self.getKota() + ", Prov. " + self.getProvinsi())
        print("  Luas\t\t: " + str(self.getLuas()) + " ha")
        if len(self.getKomoditas()) == 0:
            # jika dalam objek lahan tidak ada objek komoditas
            print("!! Lahan masih kosong")
        else:
            # jika dalam objek lahan ada objek komoditas
            no = 1
            for k in self.getKomoditas():
                print("  " + str(no) + ". ", end="")
                k.printKomoditas()
                no+=1