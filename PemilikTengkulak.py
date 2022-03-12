'''
Saya Sekar Madu Kusumawardani_2007703 mengerjakan Kuis 1 dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

# Menginport class Penduduk
from Penduduk import Penduduk # Parent dari class PemilikTengkulak

class PemilikTengkulak(Penduduk): # derived class dari class Penduduk
    # atribut private
    __idTengkulak = ""
    __komoditas = [] # satu tengkulak bisa memiliki banyak komoditas
    
    def __init__(self):
        super().__init__()
        self.__idTengkulak = ""
        self.__komoditas = [] # diisi setelah objek komoditas dibuat

    # method get set atribut
    def setIdTengkulak(self, idTengkulak):
        self.__idTengkulak = idTengkulak
    
    def getIdTengkulak(self):
        return self.__idTengkulak

    def setKomoditas(self, komoditas): # menambah objek komoditas
        self.__komoditas.append(komoditas)

    def getKomoditas(self):
        return self.__komoditas

    # method cetak data
    def printTengkulak(self):
        # Mencetak data PemilikTengkulak
        print("Id Penduduk\t: " + self.getIdPenduduk())
        print("Id Tengkulak\t: " + self.getIdTengkulak())
        print("Nama\t\t: " + self.getNama())
        if len(self.getKomoditas()) == 0:
            # jika tidak ada objek Komoditas dalam objek PemilikTengkulak
            print("Tengkulak belum memiliki komoditas") # asumsi tengkulak belum membeli komoditas
        else:
            # jika ada objek Komoditas dalam objek PemilikTengkulak
            no = 1
            for k in self.getKomoditas():
                print(str(no) + ". ", end="")
                k.printKomoditas2()
        print("------------------------------------------")