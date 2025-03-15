# Made By https://github.com/mochraiyan

def tambah_siswa(daftar_siswa):
  nama = input("Masukkan nama siswa: ")
  kelas = input("Masukkan kelas siswa: ")
  try:
    nilai = float(input("Masukkan nilai siswa"))
  except ValueError:
    print("Input nilai tidak valid. Harap masukkan angka")
    return daftar_siswa
  siswa_baru = {"nama": nama,"kelas": kelas, "nilai": nilai}
  daftar_siswa.append(siswa_baru)
  print(f"Siswa {nama} berhasil ditambahkan")
  return daftar_siswa

def tampilkan_siswa():
  if not daftar_siswa:
    print("Belum ada data siswa")
    return
  print("Data Siswa")
  print("-" * 30)
  for siswa in daftar_siswa:
    print("{:<15} {:<10} {:5.2f}".format(siswa["nama"], siswa["kelas"], siswa["nilai"]))
  print("-" * 30)

def hapus_siswa(daftar_siswa, nama_dihapus):
  ditemukan = False
  for i in range(len(daftar_siswa)):
    if daftar_siswa[i]["nama"].lower() == nama_dihapus.lower():
      del daftar_siswa[i]
      ditemukan = True
      print(f"Siswa dengan nama {nama_dihapus} berhasil dihapus.")
      return daftar_siswa

  if not ditemukan:
    print(f"Siswa dengan nama {nama_dihapus} tidak ditemukan.")


def cari_siswa(daftar_siswa, nama):
  ditemukan = False
  for siswa in daftar_siswa:
    if siswa["nama"].lower() == nama.lower():
      ditemukan = True
      print("{:<15} {:<10} {:5.2f}".format(siswa["nama"], siswa["kelas"], siswa["nilai"]))

  if not ditemukan:
    print(f"Siswa bernama {nama} tidak ditemukan!")

def hitung_rata_rata_nilai_semua_siswa(daftar_siswa):
  nilai = 0
  for siswa in daftar_siswa:
    nilai += float(siswa["nilai"])
  return nilai / len(daftar_siswa)

daftar_siswa = []

while True:
  print("Menu Manajemen Data Siswa: ")
  print("1. Tambah Siswa")
  print("2. Tampilkan Semua Siswa")
  print("3. Hapus Siswa")
  print("4. Cari Siswa")
  print("5. Hitung Rata-rata")
  print("0. Keluar")
  pilihan = input("Masukkan pilihan anda")
  if pilihan == "1":
    daftar_siswa = tambah_siswa(daftar_siswa)
  elif pilihan == "2":
    tampilkan_siswa()
  elif pilihan == "3":
    nama_dihapus = input("Siapa nama siswa yang anda ingin hapus? ")
    daftar_siswa = hapus_siswa(daftar_siswa, nama_dihapus)
  elif pilihan == "4":
    nama = input("Nama siswa yang ingin dicari?")
    cari_siswa(daftar_siswa, nama)
  elif pilihan == "5":
    nilai_rata_rata = hitung_rata_rata_nilai_semua_siswa(daftar_siswa)
    print(f"Nilai rata-rata semua siswa: {nilai_rata_rata}")
  elif pilihan == "0":
    break
  else:
    print("Pilihan tidak valid. Silahkan coba lagi.")

# tambah_siswa() fungsi dengan nilai balik
    # Alasan: karena fungsi ada nilai balik yaitu variable daftar_siswa
# tampilkan_siswa() fungsi dasar
    # Alasan: karena fungsi tidak ada nilai balik dan tidak ada parameter.
# hapus_siswa() fungsi dengan parameter dan nilai balik
    # Alasan: karena fungsi memiliki parameter dan nilai balik.