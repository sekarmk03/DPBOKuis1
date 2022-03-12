'''
Saya Sekar Madu Kusumawardani_2007703 mengerjakan Kuis 1 dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

# mengimport class Penduduk dan Lahan
from Penduduk import Penduduk # parent dari class Petani
from Lahan import Lahan # dipakai di dalam class Petani

class Petani(Penduduk): # merupakan derived class dari class Penduduk
    # atribut private
    __idPetani = ""
    __status = ""
    __lahan = [] # petani bisa punya banyak lahan, atau tidak punya lahan
    # diisi setelah objek lahan dibuat
    
    def __init__(self):
        # constructor
        super().__init__()
        self.__idPetani = ""
        self.__status = ""
        self.__lahan = [] # diisi setelah objek lahan dibuat

    # method get set atribut
    def setIdPetani(self, idPetani):
        self.__idPetani = idPetani
    
    def getIdPetani(self):
        return self.__idPetani

    def setLahan(self, lahan): # menambah objek Lahan
        self.__lahan.append(lahan)
    
    def getLahan(self):
        return self.__lahan

    def setStatus(self, status):
        self.__status = status
    
    def getStatus(self):
        return self.__status

    # method cetak data
    def printPetani(self):
        # mencetak data objek petani
        print("Id Penduduk\t: " + self.getIdPenduduk())
        print("Id Petani\t: " + self.getIdPetani())
        print("Nama\t\t: " + self.getNama())
        print("Alamat\t\t: " + self.getAlamat())
        print("Status\t\t: " + self.getStatus())
        print("Lahan\t\t: " + str(len(self.getLahan())))
        if len(self.getLahan()) == 0:
            # jika tidak ada objek lahan pada objek petani
            print("> Belum memiliki lahan.")
        else:
            # jika ada objek lahan pada objek petani
            for l in self.getLahan():
                l.printLahan()
        print("-------------------------------")
            