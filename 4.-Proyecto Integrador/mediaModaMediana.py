from interface import *


class mediModaMediana(DatosInterface):
    
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
        except: Exception("No se encontro el archivo, vuelve a llenar la encuesta o crea el archivo")

    def media(self):
        try:
            return round(sum(self.valoresEncuesta) / len(self.valoresEncuesta),2)
        except: Exception("No se pudo calcular la media, archivo vacio o inexistente")
    
    def moda(self):
        try:
            self.valoresEncuesta.sort()
            frecuencia = []
            for i in range(len(self.valoresEncuesta)):
                if self.valoresEncuesta[i] not in frecuencia:
                    frecuencia.append(self.valoresEncuesta[i])
            frecuencia.sort()
            return (frecuencia[-1])
        except: Exception("No se pudo calcular la moda, archivo vacio o inexistente")

    def mediana(self):
        try:
            self.valoresEncuesta.sort()
            if len(self.valoresEncuesta) % 2 == 0:
                return (self.valoresEncuesta[int(len(self.valoresEncuesta)/2)] + self.valoresEncuesta[int(len(self.valoresEncuesta)/2)-1]) / 2
            else:
                return self.valoresEncuesta[int(len(self.valoresEncuesta)/2)]
        except: Exception("No se pudo calcular la mediana, archivo vacio o inexistente")


c=mediModaMediana()
c.media()
c.moda
c.mediana



# ventana = tkinter.Tk()
# ventana.geometry("400x300")

# #cálculo de media
# calculoMediaTitulo = tkinter.Label(ventana, text = "Cálculo Media")
# #calculoMediaTitulo.pack(side = tkinter.TOP)
# calculoMedia = tkinter.Label(ventana, text = c.media(), fg = "blue")
# #calculoMedia.pack(side = tkinter.TOP)
# calculoMediaTitulo.grid(row=0, column=0)
# calculoMedia.grid(row=0, column=1)


# calculoModaTitulo = tkinter.Label(ventana, text = "Cálculo Moda")
# calculoModa = tkinter.Label(ventana, text = c.moda(), fg = "blue")
# calculoModaTitulo.grid(row=1, column=0)
# calculoModa.grid(row=1, column=1)


# calculoMedianaTitulo = tkinter.Label(ventana, text = "Cálculo Mediana") 
# calculoMediana = tkinter.Label(ventana, text = c.mediana(), fg = "blue")
# calculoMedianaTitulo.grid(row=2, column=0)
# calculoMediana.grid(row=2, column=1)

#ejecuto la ventana
# ventana.mainloop()

