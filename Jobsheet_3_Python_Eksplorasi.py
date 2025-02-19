# Daftar harga produk yang tersedia di toko
harga_produk = [32000, 21000, 13000, 14000]
# Daftar nama produk yang tersedia di toko
nama_produk = ['Sunco', 'So Klin', 'W', 'G']
# List kosong untuk menyimpan barang yang akan dibeli
belanjaan = []

# Fungsi untuk menampilkan daftar produk beserta harganya
def list_produk():
    print("=" * 35)  # Membuat garis pembatas
    # Looping untuk menampilkan produk dan harga
    # enumerate(start=1) digunakan agar penomoran mulai dari 1 bukan 0
    for i, np in enumerate(nama_produk, start=1):
        hp = harga_produk[i - 1] # Kenapa dikurangi satu, karena kita mulai penomoran dari angka 1, dan untuk mengakses array itu dari 0, kita kurangi 1, jadi kalau 1 - 1, berarti 0, 0 = item pertama di list.
        print(f"{i} {np} - Rp. {hp}")

# Fungsi untuk menampilkan daftar belanjaan yang sudah dipilih
def list_belanjaan():
    print("=" * 35)
    for i, belanja in enumerate(belanjaan, start=1):
        print(f"{i} {belanja[0]} - Rp. {belanja[1]}")

# Fungsi untuk menghitung total harga belanjaan
def total_belanjaan():
    total = 0
    for belanja in belanjaan:
        total += belanja[1]  # Mengambil harga dari tuple belanjaan
    return total

# Fungsi untuk menampilkan menu pilihan
def print_menu():
    list_produk()
    print('5. Gak jadi belanja deh!')
    print('6. Lihat belanjaan')
    print('7. Lanjut pembayaran')
    print('8. Hapus item belanja')

print("SELAMAT DATANG DI TOKO [ST]")

# Loop utama program
while True:
    print_menu()
    print("=" * 35)
    
    # Meminta input pilihan menu dari user
    menu = int(input(">> "))
    
    # Jika pilihan 1-4, berarti memilih produk untuk dibeli
    if menu in [1,2,3,4]:
        pilihan = menu - 1
        # Menambahkan tuple (nama_produk, harga) ke list belanjaan
        belanjaan.append((nama_produk[pilihan], harga_produk[pilihan]))
    
    # Pilihan 5: Batalkan semua belanjaan
    elif menu == 5:
        print("Cancel belanja")
        belanjaan.clear()  # Mengosongkan list belanjaan
        print(belanjaan)
        break
    
    # Pilihan 6: Lihat isi keranjang belanja
    elif menu == 6:
        if len(belanjaan) == 0:
            print('Kamu belum nambahin item apapun ke keranjang!')
            continue
        list_belanjaan()
    
    # Pilihan 7: Selesai belanja dan tampilkan total
    elif menu == 7:
        print("DETAIL BELANJA")
        print("=" * 35)
        list_belanjaan()
        print(f"Total belanja anda adalah: Rp. {total_belanjaan()}")
        print("Terimakasih telah berbelanja di toko kami! Semoga hari anda menyenangkan.")
        break
    
    # Pilihan 8: Hapus item dari keranjang
    elif menu == 8:
        if len(belanjaan) == 0:
            print('Kamu belum nambahin item apapun ke keranjang!')
            continue
        
        list_belanjaan()
        # Meminta input nomor item yang akan dihapus
        index_item_yang_dihapus = int(input("Belanjaan mana yang mau anda hapus?"))
        
        # Cek apakah nomor item valid
        if index_item_yang_dihapus > len(belanjaan):
            print("Index item yang akan di hapus tidak bisa lebih besar daripada banyaknya item belanjaan!")
            continue
        
        # Hapus item yang dipilih dan tampilkan informasi item yang dihapus
        item_dihapus = belanjaan.pop(index_item_yang_dihapus - 1)
        print(f"Produk {item_dihapus[0]} telah dihapus dari keranjang!")