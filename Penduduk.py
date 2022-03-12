'''
Saya Sekar Madu Kusumawardani_2007703 mengerjakan Kuis 1 dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

class Penduduk:
    # atribut private
    __idPenduduk = ""
    __nama = ""
    __alamat = ""

    def __init__(self):
        # constructor
        self.__idPenduduk = ""
        self.__nama = ""
        self.__alamat = ""
        
    # method get set atribut
    def setIdPenduduk(self, idPenduduk):
        self.__idPenduduk = idPenduduk
    
    def getIdPenduduk(self):
        return self.__idPenduduk

    def setNama(self, nama):
        self.__nama = nama
    
    def getNama(self):
        return self.__nama

    def setAlamat(self, alamat):
        self.__alamat = alamat
    
    def getAlamat(self):
        return self.__alamat
