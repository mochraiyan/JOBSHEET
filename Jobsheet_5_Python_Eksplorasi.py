# Made by github.com/mochraiyan

class Hero:
    def __init__(self, description, difficulty, type, weapons, damage, health, speed):
        self.description = description
        self.difficulty = difficulty
        self.type = type
        self.weapons = weapons
        self.damage = damage
        self.health = health
        self.speed = speed

    def moveDown(self, steps):
        print(f"Hero berubah posisi kebawah dengan {steps} step.")
        pass

    def moveUp(self, steps):
        print(f"Hero berubah posisi ke atas dengan {steps} step.")
        pass

    def moveRight(self, steps):
        print(f"Hero berubah posisi ke kanan dengan {steps} step.")
        pass

    def moveLeft(self, steps):
        print(f"Hero berubah posisi ke kiri dengan {steps} step.")
        pass
