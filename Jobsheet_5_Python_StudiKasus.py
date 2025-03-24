class Hero:
    def __init__(self, weapon):
        self.hp = 100
        self.damage = 0
        self.weapon = self.collectItem(weapon)

    def healing(self):
        self.hp += 10

    def attack(self, other_hero):
        if other_hero.hp < 1:
           print("Sang musuh telah tumbang kawan!")
           return

        old_hp = other_hero.hp
        other_hero.hp -= self.damage
        
        print(f"Lawan terkena serangan, hp lawan berkurang sebesar {old_hp - other_hero.hp}!")

    def collectItem(self, item):
        if item == "Pedang":
            self.damage = 10
            return "Pedang" 
        elif item == "Panah":
            self.damage = 18
            return "Panah"
        elif item == "Batu":
            self.damage = 6
            return "Batu"
        else:
            self.damage = 3
            return "Tangan"

JamesLee = Hero("Tangan")
MJ = Hero("Pedang")

while True:
    print("1. Attack MJ")
    print("2. Stat MJ")
    menu = input(">> ")
    if menu == "1":
        JamesLee.attack(MJ)
    elif menu == "2":
        print(f"MJ:\nHP: {MJ.hp}\nDamage: {MJ.damage} ({MJ.weapon})")
    else:
        break
