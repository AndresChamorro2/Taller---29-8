#Andrés Felipe Chamorro Pérez

palabra= "banana"

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

cadena_vocal= []
cadenas_cosonante= []

for i in range(len(palabra)):
    for j in range(i+1, len(palabra)+1):
        subcadena = palabra[i:j]
        if subcadena[0] in vocales:
            cadena_vocal.append(subcadena)
        else:
            cadenas_cosonante.append(subcadena)

print(f"palbra usada: (palabra)")
print(f"\nJugador A (inician con vocal)")
print(cadena_vocal)

print(f"\nJugador B(inicia con consonante):")
print(cadenas_cosonante)

if len(cadena_vocal) > len(cadenas_cosonante):
    print("\nGana Jugador A")
elif len(cadena_vocal) < len(cadenas_cosonante):
    print("\nGana jugador B")
else:
    print("\nempate")