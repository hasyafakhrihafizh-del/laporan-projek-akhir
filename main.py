class Barang:
    def __init__(self, kode, nama, harga):
        
        self.__kode = kode
        self.__nama = nama
        self.__harga = harga

 
    def get_kode(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

  
    def tampilkan_barang(self):
        print(
            f"{self.__kode} | "
            f"{self.__nama} | "
            f"Rp{self.__harga}"
        )
        