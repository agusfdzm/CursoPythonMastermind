print("¿Cuanto sabes de One Piece?")

punt = 0

print("""
Pregunta 1: ¿Que Akuma no Mi comió Luffy?\n
a) Mera Mera no Mi\n
b) Hie Hie no Mi\n
c) Gomu Gomu no Mi\n
""")

r1 = input("Introduce tu respuesta: ")
r1 = r1.lower()

if r1 == "a" or r1 == "b":
    print("HAS FALLADO! La respuesta correcta era:\n. C) Gomu Gomu no Mi")
elif r1 == "c":
    print("HAS ACERTADO!")
    punt += 10
else:
    print("Opción no válida")

print("""
Pregunta 2: ¿Cual es el objetivo de Monkey D. Luffy?\n
a) Ser el rey de los piratas\n
b) Derrotar al gobierno mundial\n
c) Vengar a su familia\n
""")

r2 = input("Introduce tu respuesta: ")
r2 = r2.lower()

if r2 == "b" or r2 == "c":
    print("Has fallado!")
elif r2 == "a":
    print("Has acertado!")
    punt += 10
else:
    print("Opción no válida")

print("""
Pregunta 3: ¿Quién fue el primer nakama en unirse a la tripulación de Luffy?\n
a) Sanji
b) Usopp
c) Zoro
""")

r3 = input("Introduce tu respuesta: ")
r3 = r3.lower()

if r3 == "a" or r3 == "b":
    print("Has fallado")
elif r3 == "c":
    print("Has acertado!")
    punt += 10
else:
    print("Opción no válida")

print(f"Tu puntuación es {punt}")