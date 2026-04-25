class Battlefield:
    def __init__(self, xy):
        self.xy = xy
        self.entity = []

    def show_mapa(self):
        self.mapa = [[0]*self.xy for _ in range(self.xy)]
        for x in self.entity:
            self.mapa[x[1]][x[2]] = x[0]
        print(self.mapa)

    def add_character(self, name, x, y):
        self.entity.append([name, x, y])

def ruch(mapa, character):
    current_x = 0
    current_y = 0
    character_x = 0
    character_y = 0
    for a in mapa:
        current_y = 0
        for b in a:
            if b == character:
                character_x = current_x
                character_y = current_y
            else:
                current_y += 1
        current_x += 1
    print(character_x, " ", character_y)


proba = Battlefield(5)
proba.add_character("s", 1, 4)
proba.add_character("d", 2, 2)
proba.show_mapa()

