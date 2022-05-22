class mediModaMediana():
    
    def __init__(self):
        file = open("numeros.txt", "r")
        self.go = file.readlines()
        self.lista = [int(i) for i in self.go]
        


    def media(self):
        print(sum(self.lista) / len(self.lista))
    
    def moda(self):
        self.lista.sort()
        frecuencia = []
        for i in range(len(self.lista)):
            if self.lista[i] not in frecuencia:
                frecuencia.append(self.lista[i])
        frecuencia.sort()
        print(frecuencia[-1])

    def mediana(self, lista):
        lista.sort()
        if len(lista) % 2 == 0:
            return (lista[int(len(lista)/2)] + lista[int(len(lista)/2)-1]) / 2
        else:
            return lista[int(len(lista)/2)]


c=mediModaMediana()

c.date()


