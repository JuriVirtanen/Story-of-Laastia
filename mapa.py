class Battlefield:
    def __init__(self, xy):
        self.xy = xy
        self.entity = []

    def show_mapa(self):
        self.mapa = [[0]*self.xy for _ in range(self.xy)]
        for x in self.entity:
            self.mapa[x[1]][x[2]] = x[0]
        for a in self.mapa:
            for b in a:
                print(b,end=' ')
            print()

    def add_character(self, name, x, y):
        self.entity.append([name, x, y])

    def move(self, name, x, y):
        for a in self.entity:
            if name == a[0]:
                a[1] += x
                a[2] += y

    def move_to(self, name, x, y):
        for a in self.entity:
            if name == a[0]:
                a[1] = x
                a[2] = y
    
    

#
#proba = Battlefield(5)
#proba.add_character("s", 1, 4)
#proba.add_character("d", 2, 2)
#proba.show_mapa()
#while True:
#    x = input()
#    if x == 'w':
#        proba.move("s", 0, -1)
#    elif x == 'n':
#        proba.move("s", -1, 0)
#    elif x == 'e':
#        proba.move("s", 0, 1)
#    elif x == 's':
#        proba.move("s", 1, 0)
#    proba.show_mapa()
#