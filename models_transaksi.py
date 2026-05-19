class Transaksi:
    def __init__(self):
        self.daftar_belanja = []

    def tambah_barang(self, barang, jumlah):

        subtotal = barang.get_harga() * int(jumlah)

        item = {
            "nama": barang.get_nama(),
            "harga": barang.get_harga(),
            "jumlah": jumlah,
            "subtotal": subtotal
        }

        self.daftar_belanja.append(item)

    def hitung_total(self):
        total = 0

        for item in self.daftar_belanja:
            total += item["subtotal"]

        return total

    def tampilkan_struk(self):

        print("\n===== STRUK BELANJA =====")

        for item in self.daftar_belanja:

            print(
                f"{item['nama']} "
                f"({item['jumlah']} x Rp{item['harga']}) "
                f"= Rp{item['subtotal']}"
            )

        print("=========================")
        print(f"TOTAL = Rp{self.hitung_total()}")