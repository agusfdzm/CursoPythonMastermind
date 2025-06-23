import random

print("Una revuelta en Impel Down ha estallado")

print("Luffy te dice que vayas con él. ¿Qué quieres hacer?")

opcion1 = input("""
a) Vas con Luffy. Nada puede salir mal con él
b) Decides seguir solo. Prefiero ser mi propio líder
Elige tu camino (a/b): """)

opcion1 = opcion1.lower()

if opcion1 == "a":
    print("Con Luffy todo irá bien...")
    print("Siguiendo la vía de escape nos encontramos a Magellan. ¿Qué hacemos?")

    opcion2 = input("""
Luffy no lo duda y le ataca.
a) Ayudas a Luffy. Es tu NAKAMA.
b) Le dejas tirado e intentas huir.
Elige tu opción (a/b): """)

    opcion2 = opcion2.lower()

    if opcion2 == "a":
        print("Todo sale bien y conseguís vencer a Magellan. Cada vez estáis más cerca de la salida.")
        print("Luffy te ofrece la Mera Mera no Mi si aciertas una operación matemática.")

        numero1 = random.randint(1, 10)
        numero2 = random.randint(2, 10)
        operacion = numero1 * numero2

        try:
            opcion3 = int(input(f"¿Cuál es el resultado correcto de {numero1} * {numero2}? "))
            if opcion3 == operacion:
                print("¡INCREÍBLE! Has conseguido la Mera Mera no Mi. Todo parece que está a punto de acabar, tenéis un poder inigualable.")
            else:
                print("Has fallado y Luffy no te da la Mera Mera.")
        except ValueError:
            print("Eso no es un número válido. Has perdido tu oportunidad.")

    elif opcion2 == "b":
        print("Luffy se queda desconcertado con tu huida. Magellan le consigue dar por la espalda y Luffy cae al suelo derrotado.")
        print("Magellan se centra en ti y te acaba matando.")
    else:
        print("Opción no válida. Magellan aprovecha tu indecisión para atacarte. Has muerto.")

elif opcion1 == "b":
    print("Decides ir por tu cuenta, pero sin ayuda ni información te pierdes en los niveles de Impel Down.")
    print("Magellan te encuentra solo y sin preparación. Has muerto.")
else:
    print("Opción no válida. En tu confusión, los guardias te atrapan. Has muerto.")
