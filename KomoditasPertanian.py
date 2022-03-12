'''
Saya Sekar Madu Kusumawardani_2007703 mengerjakan Kuis 1 dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

# mengimport class Lahan
from Lahan import Lahan # class Lahan dipakai di dalam class KomoditasPertanian

class KomoditasPertanian:
    # Objek komoditas tidak bisa dibuat tanpa ada lahan
    # saat komoditas dibuat, otomatis didaftarkan ke lahan
    # atribut private
    __idKomoditas = ""
    __namaKomoditas = ""
    __jenisLahanKomoditas = ""
    __sistemTanam = ""
    __dijual = ""

    def __init__(self):
        # constructor
        self.__idKomoditas = ""
        self.__namaKomoditas = ""
        self.__jenisLahanKomoditas = ""
        self.__sistemTanam = ""
        self.__dijual = ""

    def __init__(self, idKomoditas, namaKomoditas, lahan, dijual=""):
        # jika komoditas belum dijual, maka argumen dijual tidak perlu diisi
        # sehingga akan mengambil nilai defaultnya yaitu string kosong
        # constructor
        self.__idKomoditas = idKomoditas
        self.__namaKomoditas = namaKomoditas
        self.__jenisLahanKomoditas = lahan.getJenisTanah()
        self.__sistemTanam = lahan.getSistemTanam()
        self.__dijual = dijual
        
    # method get set atribut
    def setIdKomoditas(self, idKomoditas):
        self.__idKomoditas = idKomoditas

    def getIdKomoditas(self):
        return self.__idKomoditas

    def setNamaKomoditas(self, namaKomoditas):
        self.__namaKomoditas = namaKomoditas

    def getNamaKomoditas(self):
        return self.__namaKomoditas

    def setJenisLahanKomoditas(self, lahan): #objek lahan, mengambil data jenis lahan
        self.__jenisLahanKomoditas = lahan.getJenisTanah()

    def getJenisLahanKomoditas(self):
        return self.__jenisLahanKomoditas

    def setSistemTanam(self, lahan): # objek lahan, mengambil data sistem tanam
        self.__sistemTanam = lahan.getSistemTanam()

    def getSistemTanam(self):
        return self.__sistemTanam

    def setDijual(self, dijual):
        self.__dijual = dijual

    def getDijual(self):
        return self.__dijual

    # method cetak data
    def printKomoditas(self):
        # method ini untuk mencetak data bersama dengan Objek Lahan
        print("Id Komoditas\t: " + self.getIdKomoditas())
        print("     Nama\t\t: " + self.getNamaKomoditas())
        if len(self.getDijual()) == 0:
            print("     ! Komoditas belum dijual")
        else:
            print("     Komoditas dijual ke " + self.getDijual())

    def printKomoditas2(self):
        # method ini untuk mencetak data komoditas tanpa bersama Objek Lahan
        print("Id Komoditas\t: " + self.getIdKomoditas())
        print("   Nama\t\t: " + self.getNamaKomoditas())
        print("   Jenis Lahan\t: " + self.getJenisLahanKomoditas())
        print("   Sistem Tanam\t: " + self.getSistemTanam())
        print("----------------------------------")