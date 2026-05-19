from models_barang import Barang
from models_transaksi import Transaksi
from simpan_transaksi import simpan_transaksi

barang1 = Barang("B001", "Indomie", 3500)
barang2 = Barang("B002", "Teh Botol", 5000)
barang3 = Barang("B003", "Roti", 7000)

daftar_barang = [barang1, barang2, barang3]

transaksi = Transaksi()

while True:
    print("\n===== KASIR SEDERHANA =====")
    print("DAFTAR BARANG")

    for barang in daftar_barang:
        barang.tampilkan_barang()

    kode = input("\nMasukkan kode barang: ")

    barang_dipilih = None

    for barang in daftar_barang:
        if barang.get_kode() == kode:
            barang_dipilih = barang

    if barang_dipilih is None:
        print("Barang tidak ditemukan!")
        continue

    while True:
        try:
            jumlah = int(input("Masukkan jumlah: "))

            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue

            break

        except ValueError:
            print("Input harus berupa angka!")

    transaksi.tambah_barang(barang_dipilih, jumlah)

    lagi = input("Tambah barang lagi? (y/n): ")

    if lagi.lower() != "y":
        break


transaksi.tampilkan_struk()


total = transaksi.hitung_total()

while True:
    try:
        bayar = int(input("Masukkan uang pembayaran: "))

        if bayar < total:
            print("Uang tidak cukup!")
            continue

        break

    except ValueError:
        print("Input harus angka!")

kembalian = bayar - total

print(f"Kembalian = Rp{kembalian}")

simpan_transaksi(transaksi, bayar, kembalian)

print("Transaksi berhasil disimpan!")
print("Terima kasih telah berbelanja.")