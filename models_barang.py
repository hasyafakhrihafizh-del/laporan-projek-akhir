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



class Makanan(Barang):

    def __init__(self, kode, nama, harga, expired):

        super().__init__(kode, nama, harga)

        self.expired = expired

    def tampilkan_expired(self):

        print(f"Expired: {self.expired}")



class Minuman(Barang):

    def __init__(self, kode, nama, harga, ukuran):

        super().__init__(kode, nama, harga)

        self.ukuran = ukuran

    def tampilkan_ukuran(self):

        print(f"Ukuran: {self.ukuran}")