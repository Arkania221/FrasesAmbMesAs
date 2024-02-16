"""
Primero creamos el def, luego lo agregaremos al bucle del programa
"""

def cogerylower():
    frase = str(input("Ingrese una frase > "))
    frase = frase.lower()
    return(frase)
    

def comparar()
    fraseInicial = cogerylower()
    if fraseInicial == "fi":
        fraseFinal = "fi"
    else:
        fraseFinal = "El programa sigue"
    return(fraseFinal)

while True:
    fraseFinal = comparar()
    if fraseFinal == "fi":
        break
    else:
        print(fraseFinal)