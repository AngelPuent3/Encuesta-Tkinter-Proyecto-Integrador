from interface import *

class Diagrama(DatosInterface):

    def __init__(self):
        self.valoresEncuesta = []
        self.obtenerListaArchivo()

    def obtenerListaArchivo(self):
        try:
            archivo = open("numeros.txt", "r")
            lineaEncuestaString = archivo.readlines()[0]
            arrayEncuestaString = lineaEncuestaString.split()
            for x in arrayEncuestaString:
                self.valoresEncuesta.append(int(x))
        except: Exception("No se pudo encontrar el archivo\nVuelva a llenar la encuesta")

    def ordenar(self,undo):
        undo.sort()
        l = undo
        frecuencia = []
        for i in range(len(l)):
            t = l[i]
            frecuencia.append(t)
        return frecuencia
            
    def obtenerTallos(self,c):
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

    def resolverDiagrama(self, t, undo):
        talloYhoja = list()
        for i in t:
            for e in undo:
                d = str(e)
                if(len(d) > 2):
                    if(str(i) == d[:2]):
                        ax = [i, 0]
                        hojas = (int(d[1:3]))
                        ax[1] = hojas
                        talloYhoja.append(ax) 
                else:
                    if(str(i) == d[0]):
                        ax = [i, 0]
                        hojas = (int(d[0:1]))
                        ax[1] = hojas
                        talloYhoja.append(ax)

        return talloYhoja

    def mostrarDiagrama(self,dataraw, tallos):
        hojas = ["" for i in range(len(tallos))]
        for x in range(len(tallos)):
            for i in dataraw:
                if(i[0] == tallos[x]):
                     hojas[x] += "  "+str(i[1])

        for c in range(len(tallos)):
            print(" "+str(tallos[c]) + "    |  " + hojas[c])

    def imprimirDiagrama(self):
        valoresEncuesta = self.ordenar(self.valoresEncuesta)
        tallos = self.obtenerTallos(valoresEncuesta)
        dataraw = self.resolverDiagrama(tallos, valoresEncuesta)

        return self.mostrarDiagrama(dataraw, tallos)

d=Diagrama()
d.imprimirDiagrama()
