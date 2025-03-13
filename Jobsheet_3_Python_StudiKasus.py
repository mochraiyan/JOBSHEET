# Made By https://github.com/mochraiyan

class Pasien:
  def __init__(self, nama, umur, emergency, biaya, status):
    self.nama = nama
    self.umur = umur
    self.emergency = emergency
    self.biaya = biaya
    self.status = status
    self.lunas = False
    self.spesialis = None

list_pasien = []
history_pasien = []
SPESIALIS = ["Otak", "Jantung", "Tenggorokan", "Gigi", "Operasi", "General Doctor"]

pasien_saat_ini = None

def daftar_spesialis():
  print("=" * 32)
  for index, nama_spesialis in enumerate(SPESIALIS, start=1):
    print(f"{index}. {nama_spesialis}")
  print("=" * 32)

def daftar_pasien():
  nama_pasien = input("Nama Pasien >> ")
  umur_pasien = input("Umur Pasien >> ")
  emergency_pasien = input("Apakah Pasien Dalam Kondisi Emergency? (Y/n) ").lower()
  
  apa_emergency = "y" in emergency_pasien

  pasien = Pasien(nama_pasien, umur_pasien, apa_emergency, 0, None)

  spesialis_pasien = input("Apakah ada spesialis yang anda ingin pilih? (Y/n)").lower()

  if "y" in spesialis_pasien:
    daftar_spesialis()
    spesialis_pasien = int(input("(1-5) >> ").lower())

    if spesialis_pasien >= 6:
      pasien.spesialis = SPESIALIS[5] 
      return
    
    pasien.spesialis = SPESIALIS[spesialis_pasien]
  else:
    pasien.spesialis = SPESIALIS[5] # General Doctor

  apa_emergency = emergency_pasien == "y"

  if apa_emergency:
    list_pasien.insert(0, pasien)
  else:
    list_pasien.append(pasien)

def panggil_pasien():
  global pasien_saat_ini
  if pasien_saat_ini == None:
    pasien_saat_ini = list_pasien[0]
  else:
    print(f"{pasien_saat_ini.nama} sedang di panggil untuk pemeriksaan dokter.")

def periksa_pasien():
  global pasien_saat_ini
  global history_pasien

  if pasien_saat_ini == None:
    print(f"Tidak ada pasien yang dipanggil untuk diperiksa.")

  if pasien_saat_ini.emergency:
    pasien_saat_ini.status = "Rawat Inap"
    pasien_saat_ini.biaya = 200000
  else:
    pasien_saat_ini.status = "Rawat Jalan"
    pasien_saat_ini.biaya = 150000

  history_pasien.append(pasien_saat_ini)
  list_pasien.remove(pasien_saat_ini)
  pasien_saat_ini = None

def rekap_hari_ini():
    global pasien_saat_ini, history_pasien
    if not history_pasien and not list_pasien:
        print("Tidak ada pasien yang terdaftar hari ini!")
        return

    print("\n=== Antrian Saat Ini ===")
    if not list_pasien:
        print("Antrian kosong.")
    for i, pasien in enumerate(list_pasien, 1):
        print(f"{i}. Nama: {pasien.nama}, Emergency: {'Ya' if pasien.emergency else 'Tidak'}")

    print("\n=== Pasien Rawat Jalan ===")
    for pasien in history_pasien:
        if pasien.status == "Rawat Jalan":
            print(f"Nama: {pasien.nama}, Spesialis: {pasien.spesialis}, Lunas: {'Ya' if pasien.lunas else 'Tidak'}")

    print("\n=== Pasien Rawat Inap ===")
    for pasien in history_pasien:
        if pasien.status == "Rawat Inap":
            print(f"Nama: {pasien.nama}, Spesialis: {pasien.spesialis}, Lunas: {'Ya' if pasien.lunas else 'Tidak'}")

def pembayaran():
  global history_pasien

  if not history_pasien:
    print("Tidak ada pasien yang periksa di hari ini, tidak ada yang perlu membayar.")
    return
  
  nama_pasien = input("Siapa nama pasien yang akan membayar? >> ")

  for index, pasien in enumerate(history_pasien):
    if nama_pasien.lower() == pasien.nama.lower() and not pasien.lunas:
      pasien_emergency = "Ya" if pasien.emergency else "Tidak"
      print(f"{index:<3} \nNama: {pasien.nama:<3} \nStatus: {pasien.status:<3} \nEmergency: {pasien_emergency} \nDokter Spesialis: {pasien.spesialis} \nBiaya: {pasien.biaya}")
      print(f"TOTAL: Rp. {pasien.biaya}")
      pasien.lunas = True
      break
    elif nama_pasien.lower() == pasien.nama.lower() and pasien.lunas:
      print(f"Pasien bernama {pasien.nama} sudah lunas!")
      break

def menu():
  while True:
    print("1. Daftar Pasien")
    print("2. Panggil Pasien")
    print("3. Periksa Pasien")
    print("4. Rekap Hari Ini")
    print("5. Lanjutkan Pembayaran")

    menu_input = int(input("(1-5) >> "))

    if menu_input == 1:
      daftar_pasien()
    elif menu_input == 2:
      panggil_pasien()
    elif menu_input == 3:
      periksa_pasien()
    elif menu_input == 4:
      rekap_hari_ini()
    elif menu_input == 5:
      pembayaran()


menu()