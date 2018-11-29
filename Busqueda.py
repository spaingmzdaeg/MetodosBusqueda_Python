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


#modulo principal
opc=""
while(opc!="D"):
    print("----------MENU----------------------")
    opc=input("A)Busqueda Secuencial\nB)Busqueda binaria\nC)Busqueda por funciones hash\nD) SALIR ").upper()
    if opc == "A":

    elif opc == "B":
    elif opc == "C":







