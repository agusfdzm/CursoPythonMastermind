import readchar

myPos = [3, 1]
mapWidth = 20
mapHeight = 15
cellWidth = 4  # Tamaño horizontal de cada celda (en caracteres)

# Borde superior
print("-" * (mapWidth * cellWidth + 2))  # +2 por los bordes izquierdo y derecho

for coordinateY in range(mapHeight):
    print("|", end="")  # Borde izquierdo
    for coordinateX in range(mapWidth):
        if [coordinateX, coordinateY] == myPos:
            print("@".ljust(cellWidth), end="")  # Jugador con ancho fijo
        else:
            print(" " * cellWidth, end="")  # Espacio vacío
    print("|")  # Borde derecho

# Borde inferior
print("-" * (mapWidth * cellWidth + 2))

direction = readchar.readchar()
print(direction)