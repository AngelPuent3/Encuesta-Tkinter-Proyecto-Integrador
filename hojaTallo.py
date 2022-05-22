def Ordenar(conj):
    conj.sort()
    l = conj
    frec = []
    for i in range(len(l)):
        t = l[i]
        frec.append(t)
    return frec

def obtenerTallos(c):
    tallos = []
    conjunto = c
    for i in conjunto:
        d = str(i)
        if(len(d) > 2):
            tallos.append(int(d[:2]))
        else:
            tallos.append(int(d[0]))
    print("Conjunto:", conjunto)
    tallos = list(set(tallos))
    print("Tallos:", tallos)
    return tallos

def resolverDiagrama(t, conj):
    talloYhoja = list()
    for i in t:
        for e in conj:
            d = str(e)
            if(len(d) > 2):
                if(str(i) == d[:2]):
                    ax = [i, 0]
                    aux = (int(d[1:3]))
                    ax[1] = aux
                    talloYhoja.append(ax)
            else:
                if(str(i) == d[0]):
                    ax = [i, 0]
                    aux = (int(d[1]))
                    ax[1] = aux
                    talloYhoja.append(ax)

    return talloYhoja

def mostrarDiagrama(dataraw, tallos):
    aux = ["" for i in range(len(tallos))]
    for x in range(len(tallos)):
        for i in dataraw:
            if(i[0] == tallos[x]):
                aux[x] += "  "+str(i[1])

    for c in range(len(tallos)):
        print(" "+str(tallos[c]) + "    |  " + aux[c])


if __name__ == "__main__":
    valoresEncuesta = []
    archivo = open("numeros.txt", "r")
    lineaEncuestaString = archivo.readlines()[0]
    arrayEncuestaString = lineaEncuestaString.split()
    for x in arrayEncuestaString:
        valoresEncuesta.append(int(x))



    
    valoresEncuesta = Ordenar(valoresEncuesta)
    tallos = obtenerTallos(valoresEncuesta)
    dataraw = resolverDiagrama(tallos, valoresEncuesta)

    mostrarDiagrama(dataraw, tallos)
