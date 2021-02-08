from Interpreter import Interpreter

class Archivos():

    def __init__(self):
        self.interpreter = Interpreter()

    def definir_archivo(self, nombre, permiso):
        archivo=open(nombre, permiso)
        return archivo

    def lectura_archivo(self, archivo):
        contenido = archivo.read()
        return contenido

    def escritura_archivo(self, archivo, cadena):
        archivo.write(cadena) 

    def menu(self):

        nameEntrada = input("Input file name \n>>")

        while nameEntrada.find('.yzy') == -1:
            nameEntrada = input("File not found. Try again: \n>>")

        nameSalida = input("Output file name:  \n >>")

        while nameSalida.find('.txt') == -1:
            nameSalida = input("File not found. Try again: \n>>")

        with open(nameEntrada,"r") as f:
            lines = f.readlines()

        for s in lines:
            #print(s)
            c = self.interpreter.evaluateString(s)
            archivo2 = self.definir_archivo(nameSalida,"a")
            c= c + "\n"
            self.escritura_archivo(archivo2,c)