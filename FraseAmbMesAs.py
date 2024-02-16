"""
Primero creamos el def, luego lo agregaremos al bucle del programa
"""

def cogerylower():
    frase = str(input("Ingrese una frase > "))
    frase = frase.lower()
    return(frase)



def contabilizador(frase):
    count = 0
    for i in frase:
        if i == "a":
            count += 1
        else:
            pass
    return(count)


for i in range(1):
    fraseInicial = "o"
    fraselarga = fraseInicial
    while True:
        fraseInicial = cogerylower()
        if fraseInicial == "fi":
            break
        else:
        
         totalA = contabilizador(fraseInicial)
         
         if totalA >= contabilizador(fraselarga):
            fraselarga = fraseInicial
         else:
            pass
         print("La frase: " + str(fraselarga) + ". Es la frase con mas A's con: " + str(contabilizador(fraselarga)) + " A's")
         print(fraselarga)
         
                