class Hero:

    def __init__(self, name, speed, atk, df, hp, magic_power, luck, xp, schools):
        self.name = name
        self.speed = speed
        self.atk = atk
        self.df = df
        self.hp = hp
        self.magic_power = magic_power
        self.luck = luck
        self.xp = xp
        self.schools = schools
        self.inventory = []
        self.weapon = None

    def take_item(self, item):
        self.inventory.append(item)

    def take_weapon(self, weapon):
        self.weapon = weapon

    def show_stats(self):
        for x in self.inventory:
            self.atk += x.atk
            self.df += x.df
            self.speed += x.speed
            self.hp += x.hp
            self.luck += x.luck
            self.magic_power += x.magic_power
        self.atk += self.weapon.atk
        self.df += self.weapon.df
        self.speed += self.weapon.speed
        self.hp += self.weapon.hp
        self.luck += self.weapon.luck
        self.magic_power += self.weapon.magic_power
        print(f'Attack: {self.atk}')
        print(f'Defensive: {self.df}')
        print(f'Health Points: {self.hp}')
        print(f'Speed: {self.speed}')
        print(f'Magic Power: {self.magic_power}')
        print(f'Luck: {self.luck}')
        print(f'XP: {self.xp}')


class Weapon:
    
    def __init__(self, name, atk=0, speed=0, df=0, hp=0, magic_power=0, luck=0):
        self.name = name
        self.atk = atk
        self.speed = speed
        self.df = df
        self.hp = hp
        self.magic_power = magic_power
        self.luck = luck

class Item:

    def __init__(self, name, atk=0, speed=0, df=0, hp=0, magic_power=0, luck=0):
        self.name = name
        self.atk = atk
        self.speed = speed
        self.df = df
        self.hp = hp
        self.magic_power = magic_power
        self.luck = luck

map = [[],[],[],[],[]]


example1 = Hero("Guy", 6, 24, 24, 150, 10, 2, 0, "Woda")
example_item = Item("Afganit", atk = 10)
example_weapon = Weapon("Sztylet", atk = 1)
example1.take_item(example_item)
example1.take_weapon(example_weapon)
example1.show_stats()
