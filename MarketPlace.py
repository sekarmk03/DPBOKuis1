'''
Saya Sekar Madu Kusumawardani_2007703 mengerjakan Kuis 1 dalam mata kuliah
Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya
tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
'''

class MarketPlace:
    # atribut private
    __idMarketPlace = ""
    __namaMarketPlace = ""
    __sistemMarket = ""
    __tipeMarket = ""
    __komoditas = [] # setiap marketplace dapat memiliki banyak komoditas

    def __init__(self):
        # constructor
        self.__idMarketPlace = ""
        self.__namaMarketPlace = ""
        self.__sistemMarket = ""
        self.__tipeMarket = ""
        self.__komoditas = [] # diisi setelah objek Komoditas dibuat
    
    def __init__(self, idMarketPlace, namaMarketPlace, sistemMarket, tipeMarket):
        # constructor
        self.__idMarketPlace = idMarketPlace
        self.__namaMarketPlace = namaMarketPlace
        self.__sistemMarket = sistemMarket
        self.__tipeMarket = tipeMarket
        self.__komoditas = [] # diisi setelah objek Komoditas dibuat

    # method get set atribut
    def setIdMarketPlace(self, idMarketPlace):
        self.__idMarketPlace = idMarketPlace

    def getIdMarketPlace(self):
        return self.__idMarketPlace

    def setNamaMarketPlace(self, namaMarketPlace):
        self.__namaMarketPlace = namaMarketPlace

    def getNamaMarketPlace(self):
        return self.__namaMarketPlace

    def setSistemMarket(self, sistemMarket):
        self.__sistemMarket = sistemMarket

    def getSistemMarket(self):
        return self.__sistemMarket

    def setTipeMarket(self, tipeMarket):
        self.__tipeMarket = tipeMarket

    def getTipeMarket(self):
        return self.__tipeMarket

    def setKomoditas(self, komoditas): # menambah objek komoditas
        self.__komoditas.append(komoditas)

    def getKomoditas(self):
        return self.__komoditas

    # method cetak data
    def printMarketPlace(self):
        # mencetak data objek MarketPlace
        print("Id MarketPlace\t: " + self.getIdMarketPlace())
        print("Nama\t\t: " + self.getNamaMarketPlace())
        print("Sistem\t\t: " + self.getSistemMarket())
        print("Tipe\t\t: " + self.getTipeMarket())
        if len(self.getKomoditas()) == 0:
            # jika tidak ada objek komoditas di dalam objek marketplace
            print("MarketPlace belum memiliki komoditas")
        else:
            # jika terdapat objek komoditas di dalam objek marketplace
            no = 1
            for k in self.getKomoditas():
                print(str(no) + ". ", end="")
                k.printKomoditas2()
        print("------------------------------------")