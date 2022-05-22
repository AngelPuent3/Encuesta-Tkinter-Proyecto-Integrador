
class mediModaMediana():
    
    def __init__(self):
        self.valoresEncuesta = []



    def obtenerListaArchivo(self):
        archivo = open("numeros.txt", "r")
        lineaEncuestaString = archivo.readlines()[0]
        arrayEncuestaString = lineaEncuestaString.split()
        for x in arrayEncuestaString:
            self.valoresEncuesta.append(int(x))
 

    def media(self):
        print(sum(self.valoresEncuesta) / len(self.valoresEncuesta))
    
    def moda(self):
        self.valoresEncuesta.sort()
        frecuencia = []
        for i in range(len(self.valoresEncuesta)):
            if self.valoresEncuesta[i] not in frecuencia:
                frecuencia.append(self.valoresEncuesta[i])
        frecuencia.sort()
        print(frecuencia[-1])

    def mediana(self):
        self.valoresEncuesta.sort()
        if len(self.valoresEncuesta) % 2 == 0:
            return (self.valoresEncuesta[int(len(self.valoresEncuesta)/2)] + valores[int(len(self.valoresEncuesta)/2)-1]) / 2
        else:
            return self.valoresEncuesta[int(len(self.valoresEncuesta)/2)]


c=mediModaMediana()

c.media()
c.moda()
c.mediana()



