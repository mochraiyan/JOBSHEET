# 4. a. Class : Hero karena codecombat memiliki banyak karakter hero dan tidak mungkin membuatnya satu-satu tanpa PBO
# 4. b. Objek : Anya, karena mereka adalah instance dari class Hero dan memiliki properti dan perilaku yang sama dengan sebuah Hero tapi memilki nama yang berbeda dan statistik yang berbeda
# 4. c. Atribut : HP, Weapon, Damage, Items karena atribut ini menyimpan data yang dimiliki oleh setiap Hero
# 4. d. Method : moveRight, moveLeft, healing, attack, collect_item karena method ini adalah fungsi yang bisa dilakukan oleh setiap Hero

# class Anya:
#     def __init__(self, nama_karakter: str, posisi_x: int, posisi_y: int, nilai_kesehatan: int):
#         # --- 3. Atribut ---
#         # Atribut adalah data atau properti yang dimiliki objek
#         self.nama = nama_karakter       # Atribut: Nama karakter
#         self.x = posisi_x               # Atribut: Posisi Horizontal (seperti hero.pos.x atau hero.x di CodeCombat)
#         self.y = posisi_y               # Atribut: Posisi Vertikal (seperti hero.pos.y atau hero.y di CodeCombat)
#         self.kesehatan = nilai_kesehatan # Atribut: Nilai kesehatan (seperti hero.health)

#     def bergerak_ke(self, target_x: int, target_y: int):
#         print(f"'{self.nama}' bergerak dari ({self.x}, {self.y}) ke ({target_x}, {target_y}).")
#         self.x = target_x # Mengubah nilai atribut x
#         self.y = target_y # Mengubah nilai atribut y
#         print(f"'{self.nama}' sekarang di ({self.x}, {self.y}).")

#     def tampilkan_status(self):
#         print(f"--- Status '{self.nama}' ---")
#         print(f"Posisi: ({self.x}, {self.y})")
#         print(f"Kesehatan: {self.kesehatan}")
#         print("-------------------------")

# # --- 2. Membuat Objek ---

# hero_pemain = Anya(nama_karakter="Hero", posisi_x=10, posisi_y=10, nilai_kesehatan=100)

# hero_musuh = Anya(nama_karakter="Ogre", posisi_x=30, posisi_y=20, nilai_kesehatan=50)

# hero_pemain.tampilkan_status()
# hero_musuh.tampilkan_status()

# hero_pemain.bergerak_ke(25, 15)
# hero_musuh.bergerak_ke(28, 18)

# hero_pemain.tampilkan_status()

# print(f"\nNama hero pemain saat ini: {hero_pemain.nama}")
# print(f"Posisi musuh saat ini: {hero_musuh.x}, {hero_musuh.y}")

class Hero:
  def __init__(self, HP: int, Weapon: str, Damage: int):
    self.HP = HP
    self.Weapon = Weapon
    self.Damage = Damage
    self.items: list[str] = []
    
  def healing(self, heal_amount: int):
    self.HP += heal_amount
    print(f"Hero healed by {heal_amount}. Current HP: {self.HP}")
    
  def attack(self, target: object):
    print(f"Hero attacks {target} with {self.Weapon} for {self.Damage} damage.")
    return self.Damage
  
  def collect_item(self, item: str):
    print(f"Hero collects {item}.")
    self.items.append(item)
    return item
  
  def __str__(self):
    return f"Hero(HP={self.HP}, Weapon={self.Weapon}, Damage={self.Damage}, Items={self.items})"
    
hero1 = Hero(HP=100, Weapon="Sword", Damage=20)
hero2 = Hero(HP=80, Weapon="Bow", Damage=15)

hero1.attack(hero2)
hero2.healing(10)
hero1.collect_item("Health Potion")
print(hero1)
print(hero2)
