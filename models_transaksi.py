class Transaksi:
    def __init__(self):
        self.daftar_belanja = []

    def tambah_barang(self, barang, jumlah):
        subtotal = barang.harga * jumlah

        self.daftar_belanja.append({
            "nama": barang.nama,
            "harga": barang.harga,
            "jumlah": jumlah,
            "subtotal": subtotal
        })

    def tampilkan_struk(self):
        total = 0

        print("\n===== STRUK BELANJA =====")

        for item in self.daftar_belanja:
            print(
                f"{item['nama']} "
                f"({item['jumlah']} x Rp{item['harga']}) "
                f"= Rp{item['subtotal']}"
            )

            total += item['subtotal']

        print("==========================")
        print(f"TOTAL = Rp{total}")

        return total