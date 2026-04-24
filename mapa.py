mapa = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

def show_mapa(mapa):
    for x in mapa:
        for y in x:
            print(y, end=' ')
        print()

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
mapa[4][4] = "S"

ruch(mapa, "S")