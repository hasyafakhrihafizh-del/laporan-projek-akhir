class Barang:
    def __init__(self, kode, nama, harga):
        # Encapsulation
        self.__kode = kode
        self.__nama = nama
        self.__harga = harga

    # Getter
    def get_kode(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    # Method
    def tampilkan_barang(self):
        print(
            f"{self.__kode} | "
            f"{self.__nama} | "
            f"Rp{self.__harga}"
        )