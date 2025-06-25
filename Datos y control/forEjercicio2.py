usuario = input("Introduce una frase: ")

mayusculas = 0

for i in usuario:
    if i.isupper():
        mayusculas += 1

print(f"Tu frase tiene {mayusculas} mayusculas")