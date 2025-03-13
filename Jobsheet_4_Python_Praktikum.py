# Made By https://github.com/mochraiyan  

pendapatan = 15000000
saldo = 20000000

# Hilangnya keyword def membuatnya tidak mendeklarasikan fungsi
def pembukaan(namaAdmin, namaPT):
  print("=" * 32)
  print(f"Selamat datang di PT {namaPT}")
  print("="*32)
  print(f"Hai, Admin {namaAdmin}")
  pilih = input(f"Pendapatan kemarin adalah Rp.{pendapatan}, apakah andan ingin menambahkan pendapatan ke saldo? (y/n) ")
  if pilih == "y":
    print(f"Saldo sekarang adalah Rp. {tambah_saldo(pendapatan)}")
  else:
    print("Peringatan: pendapatan kemarin belum direkap")

def tambah_saldo(dt):
  # Kata kunci global digunakan untuk membuat variable global seperti saldo bisa diakses di scope fungsi
  global saldo
  saldo += dt
  # Ketika memiliki nilai balik, jangan lupa untuk mengembalikan nilai ke fungsi menggunakan return
  return saldo

daftar_admin = {"1345": "Nadia", "3212": "Tonny"}
admin = input("Masukkan kode pegawai = ")
# Tidak adanya pemanggilan fungsi code tidak akan berjalan
pembukaan(daftar_admin[admin], "SIDO MAKMUR SELALU") 