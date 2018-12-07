import random
class Busqueda:
    def busquedaSecuencial(self,unaLista,datoBuscar):
        pos=0
        encontrado=False
        while pos < len(unaLista) and not encontrado:
            if unaLista[pos]==datoBuscar:
                encontrado=True
            else:
                pos=pos+1
        return encontrado

    def busquedaBinaria(self,unaLista,elemento):
        primero = 0
        ultimo = len(unaLista)-1
        while(primero <= ultimo):
            centro = int((primero + ultimo)/2)
            valorCentro = unaLista[centro]
            print ("Comparando "+str(elemento)+" Con "+str(unaLista[centro]))

            if elemento == valorCentro:
                return centro
            elif elemento < valorCentro:
                ultimo = centro - 1 #con el fin de desplazarnos hacia la izquierda
            else:
                primero = centro + 1 #con el fin de desplazarnos hacia la derecha
        return -1



def llenarLista(n):
    lista = [0] * n
    for i in range(n):
        lista[i] = random.randint(0, 100)
    return lista

#modulo principal
opc=""
obj = Busqueda()
lista=llenarLista(100)
while(opc!="C"):
    print("----------MENU----------------------")
    opc=input("A)Busqueda Secuencial\nB)Busqueda binaria\nC) SALIR ").upper()
    if opc == "A":
        listaAux=lista
        print(listaAux)
        elementoBuscado = int(input("Ingrese elemento a buscar....."))
        indice = obj.busquedaSecuencial(listaAux, elementoBuscado)
        if indice != -1:
            print("Elemento " + str(elementoBuscado) + " se encuentra en la lista.")
        else:
            print("Elemento " + str(elementoBuscado) + " NO encontrado")

    elif opc == "B":
        lista.sort()#ordenamos lista previamente
        listaAux = lista
        print("lista ya ordenada")
        print(listaAux)
        elementoBuscado = int(input("Ingrese elemento a buscar....."))
        indice = obj.busquedaBinaria(listaAux,elementoBuscado)
        if indice != -1:
            print("Elemento "+str(elementoBuscado)+" se encuentra en el indice:"+str(indice))
        else:
            print("Elemento "+str(elementoBuscado)+" NO encontrado")












