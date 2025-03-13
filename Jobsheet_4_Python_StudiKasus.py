# Made By https://github.com/mochraiyan

def tampilkan_buku(daftar_buku):
  if not daftar_buku:
    print("Daftar buku kosong, ini terjadi mungkin karena anda menggunakan fitur cari_buku.")
    return

  print("Buku yang tersedia: ")
  print("-" * 32)
  for buku in daftar_buku:
    if buku['tersedia']:
      print("Kode: {:<10} Judul: {:<30} Author: {:<30} Genre: {:<20} Stok: {:<2} Tersedia: {:<3}"
            .format(buku['kode'],
                    buku['judul'], 
                    buku['penulis'], 
                    buku['genre'], 
                    buku['stok'], 
                    'Ya' if buku['tersedia'] else 'Tidak'))
      
  print("Buku yang tidak tersedia: ")
  print("-" * 32)
  for buku in daftar_buku:
    if not buku['tersedia']:
      print("Kode: {:<10} Judul: {:<30} Author: {:<30} Genre: {:<20} Stok: {:<2} Tersedia: {:<3}"
            .format(buku['kode'],
                    buku['judul'], 
                    buku['penulis'], 
                    buku['genre'], 
                    buku['stok'], 
                    'Ya' if buku['tersedia'] else 'Tidak'))


def cari_buku(daftar_buku):
  hasil_pencarian = []
  tipe_pencarian = input("Tipe Pencarian ('judul', 'genre', 'penulis') >> ").lower()
  pencarian = input("Cari >> ").lower()
  
  if tipe_pencarian not in ['judul', 'genre', 'penulis']:
    print(f"Tipe pencarian {tipe_pencarian} tidak ada dalam entry tipe pencarian!")
    return hasil_pencarian
  
  for buku in daftar_buku:
    if 'judul' in tipe_pencarian:
      judul_buku = buku['judul'].lower()
      if pencarian == judul_buku or pencarian in judul_buku:
        hasil_pencarian.append(buku)
    elif 'genre' in tipe_pencarian:
      genre_buku = buku['genre'].lower()
      if pencarian == genre_buku or pencarian in genre_buku:
        hasil_pencarian.append(buku)
    elif 'penulis' in tipe_pencarian:
      penulis_buku = ['penulis'].lower()
      if pencarian == penulis_buku or pencarian in penulis_buku:
        hasil_pencarian.append(buku)
  
  return hasil_pencarian

def tambah_buku(daftar_buku):
  kode_buku = input("Kode >> ")

  sudah_ada_kode_yang_sama = False
  for buku in daftar_buku:
    if kode_buku == buku['kode']:
      sudah_ada_kode_yang_sama = True
      break

  if sudah_ada_kode_yang_sama:
    print(f"{kode_buku} Sudah ada, tidak boleh ada duplikat kode!")
    return

  judul_buku = input("Judul >> ")
  genre_buku = input("Genre >> ")
  penulis_buku = input("Penulis >> ")
  stok_buku = int(input("Stok >> "))

  daftar_buku.append({
    "kode": kode_buku,
    "judul": judul_buku,
    "genre": genre_buku,
    "penulis": penulis_buku,
    "tersedia": not stok_buku < 1,
    "stok": stok_buku,
  })

def edit_buku(daftar_buku):
  kode_buku = input("Kode >> ")
  for buku in daftar_buku:
    if kode_buku == buku['kode']:
      buku_yang_diedit = buku
      break

  if not buku_yang_diedit:
    print(f"Buku dengan kode {kode_buku} tidak ditemukan!")
    return

  judul_buku = input("Judul >> ")
  genre_buku = input("Genre >> ")
  penulis_buku = input("Penulis >> ")
  stok_buku = int(input("Stok >> "))

  buku_yang_diedit['judul'] = judul_buku
  buku_yang_diedit['genre'] = genre_buku
  buku_yang_diedit['penulis'] = penulis_buku
  buku_yang_diedit['stok'] = stok_buku

  buku_yang_diedit['tersedia'] = not buku_yang_diedit['stok'] < 1

  print(f"Buku dengan kode {kode_buku} telah berhasil di edit!")

def pinjam_buku(daftar_buku, daftar_riwayat_peminjaman_buku):
  kode_buku = input("Kode >> ")
  
  for buku in daftar_buku:
    if kode_buku == buku['kode']:
      buku_yang_dipinjam = buku
      break
  
  if not buku_yang_dipinjam:
    print(f"Buku dengan kode {kode_buku} tidak ditemukan!")
    return
  
  if not buku_yang_dipinjam['tersedia']:
    print(f"Buku dengan kode {kode_buku} tidak tersedia untuk dipinjam!")
  if buku_yang_dipinjam['tersedia'] and not buku_yang_dipinjam['stok'] < 1:
    buku_yang_dipinjam['stok'] = buku_yang_dipinjam['stok'] - 1
    
    daftar_riwayat_peminjaman_buku.append({
      "kode": buku_yang_dipinjam['kode'],
      "judul": buku_yang_dipinjam['judul'],
      "penulis": buku_yang_dipinjam['penulis'],
      "genre": buku_yang_dipinjam['genre'],
    })

    if buku_yang_dipinjam['stok'] < 1:
      buku_yang_dipinjam['tersedia'] = False

    print(f"Buku dengan kode {kode_buku} telah berhasil dipinjam, stok berkurang 1.")
  elif buku_yang_dipinjam['tersedia'] and buku_yang_dipinjam['stok'] < 1:
    print(f"Buku dengan kode {kode_buku} tersedia, tapi stok telah habis!")

def tampilkan_daftar_riwayat_peminjaman_buku(daftar_riwayat_peminjaman_buku):
  print("Buku yang telah dipinjam: ")
  print("-" * 32)

  daftar_kode_buku = {}

  for riwayat_peminjaman_buku in daftar_riwayat_peminjaman_buku:
    if riwayat_peminjaman_buku['kode'] in daftar_kode_buku:
      daftar_kode_buku[riwayat_peminjaman_buku['kode']] = {
        'buku': riwayat_peminjaman_buku, 
        'count': daftar_kode_buku[riwayat_peminjaman_buku['kode']]['count'] + 1
      }
    else:
      daftar_kode_buku[riwayat_peminjaman_buku['kode']] = {'buku': riwayat_peminjaman_buku, 'count': 1}

  for kode, buku in daftar_kode_buku.items():
    count = buku['count']
    buku = buku['buku']
    print("Kode: {:<10} Judul: {:<30} Author: {:<30} Genre: {:<20} x{}"
          .format(kode, 
                  buku['judul'],
                  buku['penulis'], 
                  buku['genre'],
                  count))
    
daftar_buku = [
  {
      "kode": "B001",
      "judul": "Laskar Pelangi",
      "penulis": "Andrea Hirata",
      "tersedia": True,
      "genre": "Coming-of-Age",
      "stok": 8
  },
  {
      "kode": "B002",
      "judul": "Bumi Manusia",
      "penulis": "Pramoedya Ananta Toer",
      "tersedia": True,
      "genre": "Historical Fiction",
      "stok": 5
  },
  {
      "kode": "B003",
      "judul": "Pulang",
      "penulis": "Tere Liye",
      "tersedia": True,
      "genre": "Drama",
      "stok": 3
  },
  {
      "kode": "B004",
      "judul": "Ronggeng Dukuh Paruk",
      "penulis": "Ahmad Tohari",
      "tersedia": True,
      "genre": "Literary Fiction",
      "stok": 7
  },
  {
      "kode": "B005",
      "judul": "Sang Pemimpi",
      "penulis": "Andrea Hirata",
      "tersedia": True,
      "genre": "Coming-of-Age",
      "stok": 6
  },
  {
      "kode": "B006",
      "judul": "Negeri 5 Menara",
      "penulis": "Ahmad Fuadi",
      "tersedia": True,
      "genre": "Inspirational",
      "stok": 4
  },
  {
      "kode": "B007",
      "judul": "Perahu Kertas",
      "penulis": "Dee Lestari",
      "tersedia": True,
      "genre": "Romance",
      "stok": 9
  },
  {
      "kode": "B008",
      "judul": "Ayat-Ayat Cinta",
      "penulis": "Habiburrahman El Shirazy",
      "tersedia": True,
      "genre": "Romance",
      "stok": 2
  },
  {
      "kode": "B009",
      "judul": "Cantik Itu Luka",
      "penulis": "Eka Kurniawan",
      "tersedia": True,
      "genre": "Literary Fiction",
      "stok": 5
  },
  {
      "kode": "B010",
      "judul": "Dilan 1990",
      "penulis": "Pidi Baiq",
      "tersedia": True,
      "genre": "Romance",
      "stok": 10
  }
]
daftar_riwayat_peminjaman_buku = []

while True:
  kode_pengguna = input("Kode >> (admin, pengguna)").lower()
  if kode_pengguna == 'admin':
    while True:
      print("PERINGATAN: ANDA SEKARANG DALAM MODE ADMINISTRATOR!")
      print("1. Tampilkan Buku")
      print("2. Tambah Buku")
      print("3. Edit Buku")
      print("4. Cari Buku")
      print("5. Riwayat Peminjaman Buku")
      print("0. Keluar Kode Admin")

      menu = input("(0-3) >> ")
      if menu == "1":
        tampilkan_buku(daftar_buku)
      elif menu == "2":
        tambah_buku(daftar_buku)
      elif menu == "3":
        edit_buku(daftar_buku)
      elif menu == "4":
        daftar_filter_buku = cari_buku(daftar_buku)
        tampilkan_buku(daftar_filter_buku)
      elif menu == "5":
        tampilkan_daftar_riwayat_peminjaman_buku(daftar_riwayat_peminjaman_buku)
      elif menu == "0":
        break
      else:
        print(f"{menu} bukanalah valid entry untuk menu.")
  elif kode_pengguna == 'pengguna':
    while True:
      print("1. Tampilkan Buku")
      print("2. Pinjam Buku")
      print("3. Cari Buku")
      print("0. Keluar Kode Pengguna")

      menu = input("(0-2) >> ")
      if menu == "1":
        tampilkan_buku(daftar_buku)
      elif menu == "2":
        pinjam_buku(daftar_buku, daftar_riwayat_peminjaman_buku)
      elif menu == "3":
        daftar_filter_buku = cari_buku(daftar_buku)
        tampilkan_buku(daftar_filter_buku)
      elif menu == "0":
        break
      else:
        print(f"{menu} bukanlah valid entry untuk menu.")
  else:
    print(f"{kode_pengguna} bukanlah valid entry untuk kode pengguna!")
