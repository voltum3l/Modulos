#MODULAR
#Recibe Numero de filas y número de columnas y devuelve LISTA con TUPLA por cada elemento.
#Tupla = (fila,columna)
#Primera fila: A (maximo 25 "z")
#Primera Columna: 0 (sin maximo)

def GeneradorListaDeGrillas(nroFila,nroColumna):
    listaDeGrillas=[]
    if nroFila > 26 or nroFila < 1:
        print("|| Error || No se puede continuar.")
        print("Descripción: El número de filas tiene que estar en el rango de 0 a 26.")
        return listaDeGrillas
    if nroColumna <= 0:
        print("|| Error || No se puede continuar.")
        print("Descripción: El numero de columnas tiene que ser mayor que 0.")
        return listaDeGrillas
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","q","y","z"]

    for x in range(nroFila):
        for y in range(nroColumna):
            listaDeGrillas.append((letras[x],y))

    return listaDeGrillas


def GeneradorGrillaDiccionario(filas,columnas):
    diccionario={}
    listaAuxiliar=GeneradorListaDeGrillas(filas,columnas)

    if listaAuxiliar==[]:
        return diccionario

    nroElementos=len(listaAuxiliar)

    for x in range(nroElementos):
        diccionario[x]=listaAuxiliar[x]
        
    return diccionario
