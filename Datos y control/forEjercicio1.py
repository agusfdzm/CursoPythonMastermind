usuario = input("Escribe una frase: ")

espacios = 0
puntos = 0
comas = 0


for i in usuario:
    if i == " ":
        espacios += 1
    elif i == ".":
        puntos += 1
    elif i == ",":
        comas += 1

print(f"""
Tu programa tiene:\n
{espacios} espacios
{puntos} puntos
{comas} comas
""")