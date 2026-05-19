import os

def simpan_transaksi(transaksi, bayar, kembalian):

    folder = "data"

    if not os.path.exists(folder):
        os.makedirs(folder)

    path_file = os.path.join(folder, "transaksi.txt")

    file = open(path_file, "a")

    file.write("===== TRANSAKSI =====\n")

    for item in transaksi.daftar_belanja:

        file.write(
            f"{item['nama']} | "
            f"{item['jumlah']} x "
            f"{item['harga']} = "
            f"{item['subtotal']}\n"
        )

    file.write(f"Total      : Rp{transaksi.hitung_total()}\n")
    file.write(f"Bayar      : Rp{bayar}\n")
    file.write(f"Kembalian  : Rp{kembalian}\n")
    file.write("======================\n\n")

    file.close()